from django.urls import path
from edition.views import IndexView, AddView, UpdateItemView, DeleteItemView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add_post/", AddView.as_view(), name="add_post"),
    path("update_post/<pk>", UpdateItemView.as_view(), name="update_post"),
    path("delete_post/<pk>", DeleteItemView.as_view(), name="delete_post"),
]
