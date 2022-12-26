from django.shortcuts import render
from django.http import HttpResponse
from website.models import webstore


def index(request):
    return render(request, 'index.html')

def show (request):
   data = webstore.objects.all()
   return render(request, "show.html", {'data': data})



def contact(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Phone=request.POST['Phone']
        Email=request.POST['Email']
        Message=request.POST['Message']
        data = webstore.objects.create(Name=Name, Phone = Phone, Email = Email, Message= Message)
        # data=webstore(Name=Name,Phone=Phone,Email=Email,Message=Message)
        # data.save() 
        return render(request, 'Success.html')
    else:     
        return render(request, 'contact.html')    

# Create your views here and update.
#new line adde

