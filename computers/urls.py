from django.conf.urls import url
from django.urls import include
from django.urls import path
from . import views

app_name = 'computers_app'

urlpatterns = [
    path('', views.ComputerList.as_view(), name='computer_list'),
    path('new', views.ComputerCreate.as_view(), name='computer_new'),
    path('edit/<int:pk>', views.ComputerUpdate.as_view(), name='computer_edit'),
    path('delete/<int:pk>', views.ComputerDelete.as_view(), name='computer_delete'),
]
