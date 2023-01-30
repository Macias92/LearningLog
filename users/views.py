from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from users.forms import LoginForm


def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                redirect_url = request.GET.get('next', '/')
                return redirect(redirect_url)
            else:
                return render(request, 'users/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
