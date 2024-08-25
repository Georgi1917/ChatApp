from django.shortcuts import render, redirect
from chat_room.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.


def register_user(request):
    if request.method == "POST":
        reg_form = RegisterForm(request.POST)

        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data["username"]
            password = reg_form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            curr_user = request.user
            return redirect('chat_room', user_id=curr_user.id)
        else:
            return redirect('register')
    
    else:
        reg_form = RegisterForm()

        context = {
            "form": reg_form
        }

        return render(request, 'chat_room/register.html', context)

def login_user(request):
    if request.method == "POST":
        log_form = LoginForm(request.POST)
        
        if log_form.is_valid():
            username = log_form.cleaned_data["username"]
            password = log_form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                curr_user = request.user
                return redirect('chat_room', user_id=curr_user.id)
            else:
                return redirect('login')
        
        else:
            return redirect('login')

    else:

        log_form = LoginForm()

        context = {
            "form": log_form
        }

        return render(request, 'chat_room/login.html', context)

def chat_room(request, user_id):
    return render(request, "chat_room/index.html")