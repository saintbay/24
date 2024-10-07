from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile

def home(request):
    try:
        user = User.objects.create_superuser('adminnew', 'admin@example.com', 'adminnew') 
        profile = UserProfile.objects.create(user=user)
        profile.save()
    except:
        return HttpResponse('Home page')
    return HttpResponse('Home page')
    

