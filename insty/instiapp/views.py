from django.shortcuts import render
from .models import *
# Create your views here.

def homi(req):
     courses = Course.objects.all()
     return render(req,'index.html', {'courses': courses})
 
def viewcourse(req,cid):
    course=Course.objects.get(id=cid)
    return render(req,'vcourse.html',{'courses':course})