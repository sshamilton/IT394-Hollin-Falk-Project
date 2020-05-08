from django.urls import path

from . import views

app_name='users'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cadet_id>/', views.detail, name='detail'),
    path('<int:cadet_id>/update', views.update, name='update'),
    path('add', views.addcadet, name='addcadet'),
    path('addcompany', views.addcompany, name='addcompany'),
]
