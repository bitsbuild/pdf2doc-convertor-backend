from rest_framework.viewsets import ModelViewSet
from app.models import Pdf
from app.serializers import PdfSerializer
import os
from django.conf import settings
from pdf2docx import Converter
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
class PdfViewSet(ModelViewSet):
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    http_method_names = ['post']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        pdf_path = os.path.join(settings.MEDIA_ROOT,'file.pdf')
        docx_path_to_be = os.path.join(settings.MEDIA_ROOT,'result.docx')
        cv = Converter(pdf_path)
        cv.convert(docx_path_to_be)
        cv.close()
        docx_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL,'result.docx'))
        return Response({"DownloadLink":docx_url},status=HTTP_200_OK)
