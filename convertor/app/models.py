from django.db.models import Model,FileField
import os
def file_name_set(instance,filename):
    extension = filename.split('.')[-1]
    filename = f"file.{extension}"
    return filename
class Pdf(Model):
    pdf = FileField(upload_to=file_name_set)