from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name="list"),
    path('write_post/', views.write_post, name="write_post"),
    path('write_success/', views.write_success, name="write_success"),
    path('write_comment/', views.write_comment, name="write_comment"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('delete_success/', views.delete_success, name="delete_success"),
    path('update_success/', views.update_success, name="update_success"),
    path('verification/', views.verification, name="verification"),
    path('update/', views.update, name="update"),
    path('check_pwd/', views.check_pwd, name="check_pwd"),
    path('fail/', views.fail, name="fail"),
]