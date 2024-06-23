from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from .validators import validate_image_file_extension, validate_icon_image_size


def category_icon_upload_path(instance, filename):
    return f"category/{instance.id}/category_icon/{filename}"


def server_banner_upload_path(instance, filename):
    return f"server/{instance.id}/server_banner/{filename}"


def server_icon_upload_path(instance, filename):
    return f"server/{instance.id}/server_icon/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    icon = models.FileField(null=True, blank=True, upload_to=category_icon_upload_path)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        if self.id:
            existing = get_object_or_404(Category, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
        self.name = self.name.lower()
        super(Category, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="server.Category")
    def delete_category_icon(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)


class Server(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    banner = models.ImageField(
        null=True,
        blank=True,
        upload_to=server_banner_upload_path,
        validators=[validate_image_file_extension, validate_icon_image_size],
    )
    icon = models.ImageField(
        null=True,
        blank=True,
        upload_to=server_icon_upload_path,
        validators=[validate_image_file_extension, validate_icon_image_size],
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="server_owner",
    )

    categories = models.ManyToManyField(Category, related_name="categories")

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="server_members"
    )

    def save(self, *args, **kwargs):
        if self.id:
            existing = get_object_or_404(Server, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
            if existing.banner != self.banner:
                existing.banner.delete(save=False)

        super(Server, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="server.Server")
    def delete_server_icon(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)
            if field.name == "banner":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    topic = models.CharField(max_length=150, null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="channel_owner",
    )

    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="channel_server"
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="message_sender",
    )
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="message_channel"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender} - {self.content}"
