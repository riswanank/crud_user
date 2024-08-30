from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/update/<int:pk>',views.user_update,name='user_update'),
    
    path('users/edit/<int:pk>',views.user_edit,name='user_edit'),
    path('users/delete/<int:pk>',views.user_delete,name='user_delete'),
    
    
]