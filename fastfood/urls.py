from django.urls import path
from . import views

app_name = "fastfood"

urlpatterns = [
    path('pizza/', views.pizza, name="pizzas"),
    path('burger/', views.burger, name='burgers'),  # Correct path to 'burger/'
    path('order/', views.order, name='order'),
    path('success/', views.success, name='success'),
    path('signup/', views.signup, name='signup'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
   
]
