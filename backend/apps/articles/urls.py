from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register(r'articles', views.ArticleViewSet, 'articles')

urlpatterns = router.urls
