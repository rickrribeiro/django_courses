from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.db.models import Count
from .schema import server_list_docs

from .models import Server
from .serializers import ServerSerializer


class ServerListViewSet(viewsets.ViewSet):

    queryset = (
        Server.objects.all()
    )  # todo - following the course, but remember to refactor it to dont load all servers in memory

    @server_list_docs
    def list(self, request):
        """Vendo se essa parada aparece la no swagger"""
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get("with_num_members") == "true"

        if by_user:
            if request.user.is_authenticated:
                user_id = request.user.id
                self.queryset = self.queryset.filter(member=user_id)
            else:
                raise AuthenticationFailed(
                    detail="User must be authenticated to filter by user"
                )

        if by_serverid:
            try:
                self.queryset = self.queryset.get(id=by_serverid)
                if (
                    not self.queryset.exists()
                ):  # todo - following the course, but refactor this redundant raise :v
                    raise ValidationError(
                        detail=f"Server with id {by_serverid} not found"
                    )
            except ValueError:
                raise ValidationError(detail=f"Invalid server id {by_serverid}")
        if category:
            # __ is to access the category field in the model. without it is by id
            self.queryset = self.queryset.filter(category__name=category)

        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        if qty:
            self.queryset = self.queryset[: int(qty)]

        serializer = ServerSerializer(
            self.queryset, many=True, context={"with_num_members": with_num_members}
        )
        return Response(serializer.data)
