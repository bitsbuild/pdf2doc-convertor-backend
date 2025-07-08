from django.db.models import Model,FileField
class Pdf(Model):
    pdf = FileField(upload_to='')