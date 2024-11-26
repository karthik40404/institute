from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def homi(req):
     courses = Course.objects.all()
     return render(req,'index.html', {'courses': courses})
 
def viewcourse(req,cid):
    course=Course.objects.get(id=cid)
    return render(req,'vcourse.html',{'courses':course})

def contact(req):
     return render(req,'contact.html')

def placements(req):
     return render(req,'placement.html')

def sendm(req):
     if req.method=='POST':
          name=req.POST['name']
          email=req.POST['email']
          message=req.POST['message']
          data=Message.objects.create(name=name,email=email,message=message)
          data.save()
          return redirect(contact)
     else:
          return render(req,'contact.html')

def about(req):
     return render(req,'aboutus.html')