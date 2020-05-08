from django.urls import path, include
from . import views


app_name = 'codhc'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('addcomment', views.addcomment, name='addcomment'),
    path('add', views.addpost, name='addpost'),

    
    
]
