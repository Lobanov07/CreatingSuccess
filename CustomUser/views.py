from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import CustomUserEditForm
from .models import CustomUser
from Blog.views import PostListMixin, post_filter
from Blog.models import Post

User = get_user_model()

class UserProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserEditForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('Profile:view_profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = form.save()

        return redirect('Profile:view_profile', user.username)


class UserProfileView(PostListMixin):
    template_name = 'profile/view_profile.html'
    model = Post

    def get_queryset(self):
        self.author = get_object_or_404(
            User,
            username=self.kwargs['username']
        )

        return post_filter(self, 'profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.author
        return context
