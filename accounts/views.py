from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .form import LoginForm
from django.contrib.auth.decorators import login_required
from .form import LoginForm, UserRegistrationForm

# Create your views here.

def user_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return HttpResponse('Tài khoản không tồn tại')
        else:
            return HttpResponse('Tài khoản không hợp lệ')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})
    


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html' ,{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})