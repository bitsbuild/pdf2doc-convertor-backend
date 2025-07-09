from rest_framework.viewsets import ModelViewSet
from app.models import Pdf
from app.serializers import PdfSerializer
import os
from django.conf import settings
from pdf2docx import Converter
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.apps import apps
from django.http import FileResponse
class PdfViewSet(ModelViewSet):
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    http_method_names = ['post']
    def create(self, request, *args, **kwargs):
        pdf = os.path.join(settings.MEDIA_ROOT,'file.pdf')
        docx = os.path.join(settings.MEDIA_ROOT,'result.docx')
        for file_path in [pdf,docx]:
            if os.path.exists(file_path):
                os.remove(file_path)
        for model in apps.get_models():
            model.objects.all().delete()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        cv = Converter(pdf)
        cv.convert(docx)
        cv.close()
        return FileResponse(open(docx,'rb'),content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')