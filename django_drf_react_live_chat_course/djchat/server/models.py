from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from .validators import validate_icon_image_size, validate_image_file_extension


def server_icon_upload_path(instance, filename):
    return f"server/{instance.id}/server_icons/{filename}"


def category_upload_icon_path(instance, filename):
    return f"category/{instance.id}/category_icons/{filename}"


def server_banner_upload_path(instance, filename):
    return f"server/{instance.id}/server_banner/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.FileField(
        null=True, blank=True, upload_to="category_icons_upload_path"
    )

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id:  # if its updating
            existing = get_object_or_404(Category, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
        super(Category, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="server.Category")
    def category_delete_files(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)


class Server(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="server_category"
    )
    # owner = models.ForeignKey("account.Account", on_delete=models.CASCADE, related_name="server_owner")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="server_owner"
    )
    description = models.CharField(max_length=250, null=True)

    member = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="server_member", blank=True
    )

    def __str__(self):
        return f"{self.name}-{self.id}"


class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="channel_owner",
        validators=[validate_icon_image_size, validate_image_file_extension],
    )

    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="channel_server"
    )
    topic = models.CharField(max_length=250, null=True)
    banner = models.ImageField(
        upload_to=server_banner_upload_path, null=True, blank=True
    )
    icon = models.ImageField(upload_to=server_icon_upload_path, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.id:  # if its updating
            existing = get_object_or_404(Channel, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
            if existing.banner != self.banner:
                existing.banner.delete(save=False)
        super(Channel, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="server.Server")
    def channel_delete_files(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon" or field.name == "banner":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)

    def __str__(self):
        return self.name
