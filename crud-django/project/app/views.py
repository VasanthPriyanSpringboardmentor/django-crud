from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    # return HttpResponse("Hello world")
    return render(request, 'index.html')
def detail(request,post_id):
    return HttpResponse(f"You're looking at detail{post_id}")

def old_url_redirect(request):
    # return redirect("new_url")
    return redirect(reverse("app:new_url"))

def new_url_view(request):
    return HttpResponse("This is the new url")