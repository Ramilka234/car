from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegisterForm, InspectionForm, UserProfileForm, CarForm, EditInspectionForm, \
    RegistrationRequestForm, EditRegForm, ArticleForm
from .models import Inspection, Article, Car, RegistrationRequest


def index(request):
    articles = Article.objects.all()
    return render(request, 'inspection/index.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'inspection/article_detail.html', {'article': article})

def inspection_list(request):
    inspections = Inspection.objects.all()
    return render(request, 'inspection/inspection_list.html', {'inspections': inspections})

def inspection_detail(request, pk):
    inspection = get_object_or_404(Inspection, pk=pk)
    return render(request, 'inspection/inspection_detail.html', {'inspection': inspection})

def contact(request):
    return render(request, 'inspection/contact.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'inspection/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def order(request):
    user_cars = Car.objects.filter(user=request.user)

    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save(commit=False)
            car_id = request.POST.get('car')
            inspection.car = Car.objects.get(id=car_id)
            inspection.save()
            return redirect('home')
    else:
        form = InspectionForm()

    return render(request, 'inspection/order.html', {'user_cars': user_cars, 'form': form})

def order_success(request):
    return render(request, 'inspection/order_success.html')

@login_required
def profile(request):
    cars = Car.objects.filter(user=request.user)
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('profile')
    else:
        form = CarForm()
    return render(request, 'inspection/profile.html', {'cars': cars, 'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'inspection/edit_profile.html', {'form': form})


@login_required
def order(request):
    user_cars = Car.objects.filter(user=request.user)
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save(commit=False)
            car_id = request.POST.get('car')
            inspection.car = Car.objects.get(id=car_id)
            inspection.save()
            return redirect('index')
    else:
        form = InspectionForm()
    return render(request, 'inspection/order.html', {'user_cars': user_cars, 'form': form})

@login_required
def my_orders(request):
    if request.user.is_staff:
        inspections = Inspection.objects.all()
        user_requests = RegistrationRequest.objects.all()
    else:
        inspections = Inspection.objects.filter(car__user=request.user, passed=False)
        user_requests = RegistrationRequest.objects.filter(user=request.user, approved=False)
    return render(request, 'inspection/my_orders.html', {'inspections': inspections, 'user_requests': user_requests})

@login_required
def inspection_detail(request, pk):
    inspection = get_object_or_404(Inspection, pk=pk)
    return render(request, 'inspection/inspection_detail.html', {'inspection': inspection})

@login_required
def edit_inspection(request, pk):
    inspection = get_object_or_404(Inspection, pk=pk)
    if request.method == 'POST':
        form = EditInspectionForm(request.POST, instance=inspection)
        if form.is_valid():
            form.save()
            return redirect('inspection_detail', pk=pk)
    else:
        form = EditInspectionForm(instance=inspection)
    return render(request, 'inspection/edit_inspection.html', {'form': form})

@login_required
def order_reg(request):
    if request.method == 'POST':
        form = RegistrationRequestForm(request.POST, user=request.user)
        if form.is_valid():
            registration_request = form.save(commit=False)
            registration_request.user = request.user
            registration_request.save()
            return redirect('my_orders')
    else:
        form = RegistrationRequestForm(user=request.user)
    return render(request, 'inspection/registration_request.html', {'form': form})

def reg_detail(request, pk):
    inspection = get_object_or_404(RegistrationRequest, pk=pk)
    return render(request, 'inspection/reg_detail.html', {'inspection': inspection})

@login_required
def edit_reg(request, pk):
    inspection = get_object_or_404(RegistrationRequest, pk=pk)
    if request.method == 'POST':
        form = EditRegForm(request.POST, instance=inspection)
        if form.is_valid():
            form.save()
            return redirect('reg_detail', pk=pk)
    else:
        form = EditRegForm(instance=inspection)
    return render(request, 'inspection/edit_reg.html', {'form': form})

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, 'inspection/add_article.html', {'form': form})

@login_required
@user_passes_test(is_staff)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'inspection/edit_article.html', {'form': form, 'article': article})

@login_required
@user_passes_test(is_staff)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    return render(request, 'inspection/delete_article.html', {'article': article})
