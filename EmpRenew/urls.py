from django.urls import path
from . import views
urlpatterns = [
    path('edit/', views.edit, name='edit'),
    path('disp/', views.disp, name='disp'),
]
