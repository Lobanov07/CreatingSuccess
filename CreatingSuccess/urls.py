from django.contrib import admin
from django.urls import path, include, reverse_lazy

from django.views.generic.edit import CreateView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from CustomUser.forms import CustomUserCreationForm


handler404 = "Pages.views.page_not_found"
handler500 = "Pages.views.internal_server_error"

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("Blog.urls")),

    path("", include("Pages.urls")),

    path("", include("CustomUser.urls")),

    path(
        'registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,

            success_url=reverse_lazy('Pages:index'),
        ),
        name='registration',
    ),

    path(
        'login/',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(template_name='password_reset.html'),
        name='password_reset'
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'
    ),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += [re_path(r'^media/(?P<path>.*)$',
                            serve,
                            {'document_root': settings.MEDIA_ROOT}),
                    re_path(r'^static/(?P<path>.*)$',
                            serve,
                            {'document_root': settings.STATIC_ROOT}),]
