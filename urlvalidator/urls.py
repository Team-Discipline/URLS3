from rest_framework.routers import DefaultRouter

import urlvalidator.views
from urlvalidator.views import is_valid_url

router = DefaultRouter()

router.register('url', urlvalidator.views.is_valid_url(), basename='url')

urlpatterns = router.urls
