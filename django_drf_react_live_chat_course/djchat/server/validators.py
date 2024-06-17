from PIL import Image
from django.core.exceptions import ValidationError
import os


def validate_icon_image_size(image):
    if image:
        with Image.open(image) as img:
            if img.width > 70 or img.height > 70:
                raise ValidationError(
                    "Image size is too big. The maximum size allowed is 70x70"
                )


def validate_image_file_extension(image):
    ext = os.path.splitext(image.name)[1]
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    if ext not in valid_extensions:
        raise ValidationError(
            "Invalid file extension. Please upload a valid image file."
        )
