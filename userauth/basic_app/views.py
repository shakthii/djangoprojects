from django.shortcuts import render
from basic_app.models import UserProfile
from basic_app.forms import UserForm,UserProfileForm


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,"basic_app/index.html",{'text':'my custom filter'})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #saving the data entered in user_form to db models
            userobj =user_form.save()
            userobj.set_password(userobj.password)
            userobj.save()

            profile=profile_form.save(commit=False)
            profile.userobj= userobj

            if 'portfolio_pics' in request.FILES:
                profile.portfolio_pics =request.FILES['portfolio_pics']

            profile.save()

            registered =True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,"basic_app/register.html",{'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                #return ('Logged in')
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})
@login_required
def user_logout(request):
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))
