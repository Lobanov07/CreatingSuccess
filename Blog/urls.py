from django.urls import path

from . import views

app_name = "Blog"

urlpatterns = [

    path(
        "posts/<int:post_id>/",
        views.PostDetailView.as_view(),
        name="post_detail"),

    path(
        'posts/<int:post_id>/edit/',
        views.PostUpdateView.as_view(),
        name='edit_post'),

    path(
        'posts/<int:post_id>/delete/',
        views.PostDeleteView.as_view(),
        name='delete_post'),

    path('posts/create/',
         views.PostCreateView.as_view(),
         name="create_post"),

    path(
        'category/<slug:category_slug>/',
        views.CategoryListView.as_view(),
        name='category_posts',
    ),

    path(
        'categories/',
        views.CategoryAllListView.as_view(),
        name='category_list'),

    path(
        'posts/<int:post_id>/comment/',
        views.CommentCreateView.as_view(),
        name='add_comment',
    ),
    path(
        'posts/<int:post_id>/edit_comment/<int:comment_id>/',
        views.CommentUpdateView.as_view(),
        name='edit_comment',
    ),
    path(
        'posts/<int:post_id>/delete_comment/<int:comment_id>/',
        views.CommentDeleteView.as_view(),
        name='delete_comment',
    ),
]