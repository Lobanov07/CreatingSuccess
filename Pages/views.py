from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from Blog.models import Post
from Blog.views import post_filter

User = get_user_model()


POSTS_PER_PAGE = 10


class PostListMixin(ListView):
    paginate_by = POSTS_PER_PAGE


class HomePage(PostListMixin):
    model = Post

    template_name = 'blog/index.html'
    ordering = 'id'

    def get_queryset(self):
        queryset = post_filter(self)
        print(queryset)  # Для отладки
        return post_filter(self)


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


def page_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'errors/403csrf.html', status=403)


def internal_server_error(request):
    return render(request, 'errors/500.html', status=500)
