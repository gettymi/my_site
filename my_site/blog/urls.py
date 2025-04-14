from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",views.index_page,name="index"),
    path("posts/",views.all_posts,name="all_posts"),
    path("posts/<slug:slug>/",views.post_detail,name="post_detail"),
]
