from django.shortcuts import render,redirect
from .models import Pizza, Burger
from django.http import JsonResponse
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import LoginForm 
from django.contrib.auth import authenticate, login,logout
import logging


logger = logging.getLogger('django')


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
    request.session.set_expiry(0)  # Session will expire when the browser is closed
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'POST':
        note = request.POST.get('note')
        order = request.POST.get('order')

        request.session['note'] = note
        request.session['order'] = order

        print(f'Received note: {note}')
        print(f'Received order: {order}')

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
            # Automatically log in the user after signup
            # login(request, user)
            messages.success(request, 'Signup successful! You are now logged in.')
            print("Form is valid and user is logged in.")  # Debug statement
            return redirect('index')  # Redirect to the success page
        else:
            messages.error(request, 'There was an error in your signup form. Please try again.')
            print("Form is invalid.")  # Debug statement
    else:
        form = SignUpForm()
        print("GET request - rendering signup form.")  # Debug statement
    
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
                return redirect('index')  # Redirect to a success page.
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


