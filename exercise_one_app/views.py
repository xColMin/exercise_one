from django.shortcuts import render
from django.http import HttpResponse
from exercise_one_app.models import User


# Create your views here.

def home(request):
    return render(request, 'exercise_one_app/home.html')
    
def user(request):
    
    user_list = User.objects.all()

    user_dict = {'user_list': user_list}
    
    return render(request, 'exercise_one_app/user.html', context=user_dict)
    

