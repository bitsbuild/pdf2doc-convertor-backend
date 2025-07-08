from django.db.models import Model,FileField
class PDF(Model):
    pdf = FileField(upload_to='')