from django.urls import path

from blog import views

urlpatterns = [
    path('posts',view=views.get_all_blogs),
    path('posts/<int:id>',view=views.get_blog_with_id)
]