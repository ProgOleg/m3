from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views import *

urlpatterns = [
    path('', IndexPage.as_view(), name="index_pg"),
    path("oder_approval/", oder_approval, name="oder_approval_url"),
    path("comments_approval/", comments_approval, name="comments_approval_url"),
    path("subscribe/", subscribe, name="subscribe_url")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
