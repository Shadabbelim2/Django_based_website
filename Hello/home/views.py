from django.shortcuts import render , redirect
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

def show(request):
     queryset=Contect.objects.all()
     if request.GET.get('search'): 
        queryset=queryset.filter(name__icontains = request.GET.get('search'))
     context={'contect' : queryset}
     return render(request , 'show.html' , context )

def delete(request , id):
     queryset=Contect.objects.get(id = id)
     queryset.delete()
     return redirect('show')

def edit(request , id):
     queryset = Contect.objects.get(id = id )
     if request.method == "POST" :
          name =request.POST.get('name')
          email =request.POST.get('email')
          phone =request.POST.get('phone')
          desc =request.POST.get('desc')

          queryset.name=name
          queryset.email = email
          queryset.phone = phone
          queryset.desc = desc
          queryset.date = datetime.today()
          
          print(queryset.name,  queryset.email)
          
          queryset.save()

          return redirect('show')
     context = {'contect' : queryset}
     return render(request , 'update.html' , context)