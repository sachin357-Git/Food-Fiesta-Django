from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib import messages

from .models import *

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    return render(request, 'prouser/index.html')

@login_required(login_url='/login/')
def about(request):
    return render(request, 'prouser/about.html')

@login_required(login_url='/login/')
def menu(request):
    return render(request, 'prouser/menu.html')

@login_required(login_url='/login/')
def dishdetail(request):
    return render(request, 'prouser/dishdetail.html')

@login_required(login_url='/login/')
def gallery(request):
    return render(request, 'prouser/gallery.html')

@login_required(login_url='/login/')
def chef(request):
    return render(request, 'prouser/chef.html')

@login_required(login_url='/login/')
def booktable(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        guests = request.POST.get("guests")
        date = request.POST.get("date")
        time = request.POST.get("time")
        message = request.POST.get("message")


        if not name or not email or not phone or not guests or not date or not time:

            messages.error(request, "Please fill all required fields!")

            return render(request, "prouser/booktable.html")


        b = Booking()

        b.name = name
        b.email = email
        b.phone = phone
        b.guests = guests
        b.date = date
        b.time = time
        b.message = message

        b.save()

        return redirect('/booking-success/')


    return render(request, "prouser/booktable.html")

@login_required(login_url='/login/')
def booking_success(request):
    return render(request, 'prouser/booking_success.html')

@login_required(login_url='/login/')
def feedback(request):

    if request.method == "POST":

        f = Feedback()

        f.name = request.POST.get("name")
        f.email = request.POST.get("email")
        f.rating = request.POST.get("rating")
        f.message = request.POST.get("message")

        f.save()
        messages.success(request, "Thank you for your valuable feedback!")

    return render(request, 'prouser/feedback.html')

@login_required(login_url='/login/')
def contact(request):

    if request.method == "POST":

        c = tblcontact()

        c.name = request.POST.get("name")
        c.email = request.POST.get("email")
        c.message = request.POST.get("message")

        c.save()

        messages.success(request,"Your message has been sent successfully!")

    return render(request, 'prouser/contact.html')

def login(request):

    if request.method == "POST":

        email=request.POST.get("email")
        password=request.POST.get("password")

        user_obj=User.objects.filter(email=email).first()

        if user_obj:
            user = authenticate(
                username=user_obj.username,
                password=password
            )
        else:
            user = None


        if user:

            auth_login(request,user)

            print("LOGIN SUCCESS")
            print(request.user)

            return redirect('/')

        else:
            print("LOGIN FAILED")
            messages.error(request,"Invalid email or password")

    return render(request,'prouser/login.html')


def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request,"Passwords do not match")
        elif User.objects.filter(username=email).exists():
            messages.error(request,"Email already registered")

        else:

            user = User.objects.create_user(
                username=email,
                first_name=name,
                email=email,
                password=password
            )

            user.save()

            messages.success(request,"Registration successful! Please login.")

    return render(request,'prouser/register.html')

def user_logout(request):

    logout(request)

    print("LOGIN SUCCESS")

    return redirect('/login/')

@login_required(login_url='/login/')
def owner(request):
    return render(request, 'prouser/owner.html')

