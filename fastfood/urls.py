from django.urls import path
from . import views


app_name = "fastfood"

urlpatterns = [
    path('pizza/', views.pizza, name="pizzas"),
    path('burger/', views.burger, name='burgers'),  
    path('order/', views.order, name='order'),
    path('success/', views.success, name='success'),
    path('signup/', views.signup, name='signup'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
   
    
    # Rest api url Post
    path('createpizza/', views.PizzaCreate.as_view(), name='create-pizza'),
    path('createburger/', views.BurgerCreate.as_view(), name='create-burger'),
    path('createOrder/', views.OrderCreate.as_view(), name='order-create'),
    
    # delete api
      path('delete/<int:id>/pizza/', views.PizzaDelete.as_view(), name="delete-pizza"), 
      path('delete/<int:id>/burger/', views.BurgerDelete.as_view(), name="delete-burger"),
      path('order/<int:id>/', views.OrderDetail.as_view(), name="order-detail"),
      
    # get api
     path('get/<int:id>/pizza/', views.PizzaDetail.as_view(), name="get-pizza"),  
     path('burger/<int:id>/', views.BurgerDetail.as_view(), name="burger-detail"),
     path('orderdata/', views.GetOrderDetail.as_view(), name="order-detail"),
    
    
    
    
  
]
