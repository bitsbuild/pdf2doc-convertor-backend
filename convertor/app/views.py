from rest_framework.viewsets import ModelViewSet
from app.models import Pdf
from app.serializers import PdfSerializer
class PdfViewSet(ModelViewSet):
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)