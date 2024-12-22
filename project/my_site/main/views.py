from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def community(request):
    return render(request, "main/community.html")

def create(request):
    return render(request, "main/create.html")

def join(request):
    return render(request, "main/join.html")

def login(request):
    return render(request, "main/login.html")