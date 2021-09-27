from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from baskets.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Geekshop - Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Geekshop - Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST,
                               files=request.FILES,
                               instance=request.user)  # instance - обновит данные, а не создаст новую запись
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    baskets = Basket.objects.filter(user=request.user)
    products_count = 0
    products_sum = 0
    for basket in baskets:
        products_count += basket.quantity
        products_sum += basket.quantity * basket.product.price
    context = {
        'title': 'Geekshop - Профайл',
        'form': UserProfileForm(instance=request.user),  # instance - заполнит поля текущими значениями
        'baskets': baskets,
        'products_count': products_count,
        'products_sum': products_sum
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
