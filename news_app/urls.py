from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('news/<int:news_id>/', views.news_detail_view, name='detail'),
    path('news/add/', views.add_news_view, name='add'),
    path('news/success/', views.success_view, name='success'),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view (template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('news/<int:news_id>/edit/', views.news_edit_view, name='edit'),
    path('news/<int:news_id>/delete/', views.news_delete_view, name='delete'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/delete/', views.profile_delete_view, name='profile_delete'),
]