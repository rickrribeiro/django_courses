from rest_framework import serializers

from .models import Server, Category, Channel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):
    num_members = serializers.SerializerMethodField()
    channel_server = ChannelSerializer(
        many=True, read_only=True
    )  # has to be the same name as the related_name in the model
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Server
        # fields = ["id", "name"]

        #    fields = "__all__"
        # read_only_fields = ["id"]

        exclude = ["members"]  # all - member

    def get_num_members(self, obj):
        if hasattr(obj, "num_members"):
            return obj.num_members

    def to_representation(self, instance):  # function to manipulate the serialized data
        data = super().to_representation(instance)
        with_num_members = self.context.get("with_num_members")
        if not with_num_members:
            data.pop("num_members")
        return data
