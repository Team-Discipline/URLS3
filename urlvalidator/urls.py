from rest_framework.routers import DefaultRouter

import urlvalidator.views
from urlvalidator.views import ValidateUrl

router = DefaultRouter()

router.register('url', ValidateUrl, basename='url')

urlpatterns = router.urls
