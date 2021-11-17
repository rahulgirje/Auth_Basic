from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm
from .models import UserRegistrationModel
from django.shortcuts import render, redirect




def home(request):
    template_name = 'firstapp/base.html'
    return render(request, template_name)
def registerView(request):
    form = UserRegistrationForm()
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

            '''
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            '''
            return HttpResponse('resister succefully')
    template_name='firstapp/register.html'
    context ={'form':form}
    return render(request,template_name,context)

def loginView(request):
    if request.method =='POST':
        u =request.POST.get('uname')
        p=request.POST.get('password')
        user = authenticate(username=u, passaword=p)
        if user is not None:
            login(request,user)
            return redirect('#')
        else:
            messages.error(request,'invalid data enter')

    template_name='firstapp/login.html'
    context={}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')
