from rest_framework.routers import DefaultRouter
from app.views import PdfViewSet
router = DefaultRouter()
router.register(r'pdf',PdfViewSet,basename='pdf')
urlpatterns = router.urls