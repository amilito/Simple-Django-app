from django.urls import path
from . import views

app_name = 'waste_segregation_app'
urlpatterns = [
    path('', views.new_trash, name='new_trash'),
    path('bin/', views.check_bin, name='bin'),
]