from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import UserProfileEditView, UserProfileView

app_name = 'Profile'

urlpatterns = [
    path(
        'view/<str:username>/',
        UserProfileView.as_view(),
        name='view_profile'
    ),
    path(
        'edit/<str:username>/',
        UserProfileEditView.as_view(),
        name='edit_profile'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
