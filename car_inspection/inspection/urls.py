from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('inspections/', views.inspection_list, name='inspection_list'),
    path('inspections/<int:pk>/', views.inspection_detail, name='inspection_detail'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='inspection/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('order/', views.order, name='order'),
    path('order-success/', views.order_success, name='order_success'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('inspection/<int:pk>/', views.inspection_detail, name='inspection_detail'),
    path('inspection/<int:pk>/edit/', views.edit_inspection, name='edit_inspection'),
    path('registration_request/', views.order_reg, name='registration_request'),
    path('registration_request/<int:pk>/', views.reg_detail, name='reg_detail'),
    path('registration_request/<int:pk>/edit/', views.edit_reg, name='edit_reg'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/<int:pk>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:pk>/', views.delete_article, name='delete_article'),
]