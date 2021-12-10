from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:department_id>/', views.detail, name='department'),
    
]