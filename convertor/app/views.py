from rest_framework.viewsets import ModelViewSet
from app.models import Pdf
from app.serializers import PdfSerializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
class PdfViewSet(ModelViewSet):
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        fileurl = os.path.join(settings.MEDIA_URL,'file.pdf')
        return Response({
            "Download-Link":fileurl
        },status=HTTP_200_OK)