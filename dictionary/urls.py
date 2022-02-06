from rest_framework import routers
from .api import WordViewSet

router = routers.DefaultRouter()
router.register('api/words', WordViewSet, 'words')

urlpatterns = router.urls