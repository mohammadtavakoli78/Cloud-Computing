from django.urls import path

from mysite import views

urlpatterns = [
    path("", views.main_page, name='main_page'),
    path("<str:url>", views.url_page),
    path("delete/<str:url>", views.destroy, name='destroy_now'),
    path("read_and_destory/<str:url>", views.read_and_destroy),
    path("read/<str:url>", views.read_note, name='read_note')
]
