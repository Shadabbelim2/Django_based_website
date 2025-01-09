from django.shortcuts import render 
from datetime import datetime
from home.models import Contect
from django.contrib import messages
# Create your views here.
def index(request):
   
    return render(request , 'index.html')
def about(request):
    return render(request , 'about.html')
def services(request):
     return render(request , 'services.html')
def contect(request):
     if request.method == "POST" :
          name =request.POST.get('name')
          email =request.POST.get('email')
          phone =request.POST.get('phone')
          desc =request.POST.get('desc')
          contect=Contect(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
          contect.save()
          messages.success(request, "Your Message Send Successfully!.")
     return render(request , 'contect.html')
