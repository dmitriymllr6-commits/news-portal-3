from rest_framework.routers import DefaultRouter
from .viewsets import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = router.urls