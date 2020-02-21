from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page1',views.Page1),
    path('page2',views.Page2),
]
