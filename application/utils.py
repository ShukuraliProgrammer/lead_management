from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def file_upload_validator(file_obj, file_type="document"):
    """
    Custom validator to check the file type and format.
    """

    valid_file_types = ["document"]
    image_types = ("jpeg", "png", "jpg", "svg", "webp")
    video_types = ["mp4"]
    audio_types = ["mp3"]
    document_types = [
        "pdf",
        "doc",
        "docx",
        "ppt",
        "pptx",
        "txt",
        "zip",
        "rar"
    ]
    file_extension = file_obj.name.split(".")[-1].lower()

    if file_type not in valid_file_types:
        raise ValidationError(_(f"Wrong File type. Allowed types are: {', '.join(valid_file_types)}"))

    if file_type == "image" and file_extension not in image_types:
        raise ValidationError(_("Invalid image format. Supported formats are: jpg, jpeg, png, svg, webp"))

    elif file_type == "video" and file_extension not in video_types:
        raise ValidationError(_("Invalid video format. Supported format is: mp4"))

    elif file_type == "document" and file_extension not in document_types:
        raise ValidationError(
            _("Invalid document format. Supported formats are: pdf, doc, docx, ppt, pptx, txt")
        )
    elif file_type == "audio" and file_extension not in audio_types:
        raise ValidationError(_("Invalid audio format. Supported format is: mp3"))

