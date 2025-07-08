from django.db.models import Model,FileField
from django.core.exceptions import ValidationError
import os
def file_name_set(instance,filename):
    extension = filename.split('.')[-1]
    filename = f"file.{extension}"
    return filename
def validate_pdf(file):
    if not file.name.endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")
    if file.content_type != 'application/pdf':
        raise ValidationError("Invalid file type.")
class Pdf(Model):
    pdf = FileField(upload_to=file_name_set,validators=[validate_pdf])