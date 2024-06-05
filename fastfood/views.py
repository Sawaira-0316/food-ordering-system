from argparse import Action
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer,PizzaSerializer, BurgerSerializer

from django.shortcuts import render,redirect
from .models import Pizza, Burger, Order
from django.http import JsonResponse
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import LoginForm 
from django.contrib.auth import authenticate, login,logout
import logging

logger = logging.getLogger('django')

# ====================================
# ***** POST : Create Order Api *****
# ====================================
class OrderCreate(APIView):
    def post(self, request, format=None):
        logger.info("Received a POST request to create an order.") #informational message
        serializer = OrderSerializer(data=request.data)
        
        if serializer.is_valid():
            logger.info("Order data is valid. Saving the order.")
            order = serializer.save()  
            logger.info(f"Order {order.id} created successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        logger.error("Invalid order data received.")
        logger.error(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
        
# ====================================
# ***** POST : Create Pizza Api *****
# ====================================

class PizzaCreate(APIView):
    def post(self, request, format=None):
        logger.info("Received a POST request to create a pizza.")
        serializer = PizzaSerializer(data=request.data)
        
        if serializer.is_valid():
            logger.info("Pizza data is valid. Saving the pizza.")
            pizza = serializer.save()
            logger.info(f"Pizza {pizza.id} created successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        logger.error("Invalid pizza data received.")
        logger.error(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ====================================
# ***** POST : Create Burger Api *****
# ====================================
class BurgerCreate(APIView):
    def post(self, request, format=None):
        logger.info("Received a POST request to create a burger.")
        serializer = BurgerSerializer(data=request.data)
        
        if serializer.is_valid():
            logger.info("Burger data is valid. Saving the burger.")
            burger = serializer.save()
            logger.info(f"Burger {burger.id} created successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        logger.error("Invalid burger data received.")
        logger.error(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    
# ====================================
# **** DELETE : Remove Burger Api ****
# ====================================  
class BurgerDelete(APIView):
    def delete(self, request, id, format=None):
        logger.info(f"Received DELETE request for Burger ID: {id}")
        try:
            burger = Burger.objects.get(id=id)
            logger.info(f"Found Burger: {burger}")
            burger.delete()
            logger.info(f"Deleted Burger ID: {id}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Burger.DoesNotExist:
            logger.warning(f"Burger ID: {id} not found")
            return Response({'error': 'Burger not found'}, status=status.HTTP_404_NOT_FOUND)

        
        
 # ====================================
# **** DELETE : Remove Pizza Api ****
# ====================================     
        
class PizzaDelete(APIView):
    def delete(self, request, id, format=None):
        logger.info(f"Received DELETE request for Pizza ID: {id}")
        try:
            pizza = Pizza.objects.get(id=id)
            logger.info(f"Found Pizza: {pizza}")
            pizza.delete()
            logger.info(f"Deleted Pizza ID: {id}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pizza.DoesNotExist:
            logger.warning(f"Pizza ID: {id} not found")
            return Response({'error': 'Pizza not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
 # ====================================
# **** DELETE : Remove order Api ****
# ====================================
class OrderDetail(APIView):
    def delete(self, request, id, format=None):
        logger.info(f"Received DELETE request for Order ID: {id}")
        try:
            order = Order.objects.get(id=id)
            logger.info(f"Found Order: {order}")
            order.delete()
            logger.info(f"Deleted Order ID: {id}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            logger.warning(f"Order ID: {id} not found")
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

   
 
# ====================================
# ****  get Pizza Api ****
# ====================================       
        
class PizzaDetail(APIView):
    def get(self, request, id, format=None):
        logger.info(f"Received GET request for Pizza ID: {id}")
        try:
            pizza = Pizza.objects.get(id=id)
            logger.info(f"Found Pizza: {pizza}")
            pizza_data = {
                'id': pizza.id,
                'name': pizza.name,
                'priceM': pizza.priceM,
                'priceL': pizza.priceL,
                'pImage': pizza.pImage,
            }
            return Response(pizza_data, status=status.HTTP_200_OK)
        except Pizza.DoesNotExist:
            logger.warning(f"Pizza ID: {id} not found")
            return Response({'error': 'Pizza not found'}, status=status.HTTP_404_NOT_FOUND)



  # ====================================
# ****  : get Burger Api ****
# ====================================


class BurgerDetail(APIView):
    def get(self, request, id, format=None):
        logger.info(f"Received GET request for Burger ID: {id}")
        try:
            burger = Burger.objects.get(id=id)
            logger.info(f"Found Burger: {burger}")
            burger_data = {
                'id': burger.id,
                'name': burger.name,
                'priceM': burger.priceM,
                'priceL': burger.priceL,
                'pImage': burger.pImage,
            }
            return Response(burger_data, status=status.HTTP_200_OK)
        except Burger.DoesNotExist:
            logger.warning(f"Burger ID: {id} not found")
            return Response({'error': 'Burger not found'}, status=status.HTTP_404_NOT_FOUND)
        
    
        
class GetOrderDetail(APIView):
    def get(self, request, format=None):
        logger.info("Get all order details")
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            logger.info(f"Found order data: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            logger.warning("No orders found")
            return Response({'error': 'No orders found'}, status=status.HTTP_404_NOT_FOUND)
     

def index(request):
    ctx = {'active_link': 'index'}
    return render(request, 'index.html')

def pizza(request):
    request.session.set_expiry(0) 
    pizzas = Pizza.objects.all()
    ctx = {'pizzas': pizzas, 'active_link': 'pizzas'}
    return render(request, 'pizza.html', ctx)

def burger(request):
    request.session.set_expiry(0) 
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers, 'active_link': 'burgers'}
    return render(request, 'burger.html', ctx)

@csrf_exempt
def order(request):
    request.session.set_expiry(0)  
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'POST':
        note = request.POST.get('note')
        order = request.POST.get('order')

        request.session['note'] = note
        request.session['order'] = order

        data = {
            'message': f'Received note: {note} and order: {order}'
        }
        return JsonResponse(data)
    else:
        return render(request, 'order.html')

def success(request):
       return render(request, 'success.html')






def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Signup successful! You are now logged in.')
            print("Form is valid and user is logged in.")  
            return redirect('index')  
        else:
            messages.error(request, 'There was an error in your signup form. Please try again.')
            print("Form is invalid.") 
    else:
        form = SignUpForm()
        print("GET request - rendering signup form.")  
    
    return render(request, 'signup.html', {'form': form})

def success1(request):
    return render(request, 'success1.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('index') 
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def success1(request):
    return render(request, 'success1.html')



def logout_view(request):
    logout(request)
    return redirect('index') 


