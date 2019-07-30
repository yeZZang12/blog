from django.urls import path
from . import views
import blog.views

urlpatterns = [
    path('', views.home, name="home"), 
    path('<int:blog_id>/', views.detail, name="detail"), 
    # path('new/', views.new, name="new"),
    path('blog/new/', views.new, name='new'),
    path('blog/view/', views.view, name='view'),
    
    # path('blog/create/', views.create, name='create'),
    ] 