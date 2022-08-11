from django.shortcuts import render

# from trainningproject.pages.models import Login

# from django.http import HttpResponse
# Create your views here.

x = {
    'name':"ali",
    "age":26,
    }
def index(request):
    return render(request,'pages/index.html',x)


def about(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    data=Login(username=username,password=password)
    data.save()

    return render(request,'pages/about.html')
