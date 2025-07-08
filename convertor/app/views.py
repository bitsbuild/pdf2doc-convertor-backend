from django.shortcuts import render
from rest_framework.decorators import api_view
@api_view(['POST'])
def convert_pdf_to_docx(request):
    return 0