from rest_framework.serializers import ModelSerializer
from app.models import Pdf
class PdfSerializer(ModelSerializer):
    class Meta:
        model = Pdf
        fields = '__all__'