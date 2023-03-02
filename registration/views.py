from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings as conf_settings
from .forms import RegistrationAccountForm,LoginForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def registrationView(request):
    template_name = 'registration/user_registration.html'
    form = RegistrationAccountForm()
    if request.POST:
        form = RegistrationAccountForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.save(commit=False)
            form.save()

            activation_url = 'http://127.0.0.1:8000/auth/activate/{}'.format(data.uuid)
            send_mail(
                'user activattion',
                activation_url,
                conf_settings.EMAIL_HOST_USER,
                [data.email],
                fail_silently=False,
            )
            msg = 'your user is created and ativation link is sent to {}'.format(data.email)
            messages.success(request, msg)

        else:
            print(form.errors)

    context = {
        'form':form

    }
    return render(request,template_name,context)

def loginView(request):
    template_name = 'registration/login.html'
    form = LoginForm()
    print('test--1')
    if request.POST:
        print('test--2')
        form=LoginForm(request.POST)
        if form.is_valid():
            print('test--3')
            # just verifies the login information
            data = form.cleaned_data
            user = authenticate(email=str(data['email']), password=str(data['password']))
            print(user,data,str(data['email']),str(data['password']))
            if user is not None:
                print('test--4')
                login(request,user)
                return redirect('products:product-list')
        else:
            print('test--5')
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request,template_name,context)

def acitivate_url(request,uuid):
    user = User.objects.get(uuid=uuid)
    user.is_active = True
    user.save()
    print('user activaciashi shemovida')
    return HttpResponse('your user is successfuly activated')
