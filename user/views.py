from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(req):
    cdata=cities.objects.all().order_by('-id')
    pdata=addplace.objects.all().order_by('id')
    sdata=slider.objects.all().order_by('-id')
    mydict={"city":cdata,"place":pdata,"slider":sdata}

    return render(req,'user/home.html',mydict)

def about(req):
    return render(req,'user/aboutus.html')

def imagegallery(req):
    gdata=gallery.objects.all().order_by('-id')
    return render(req,'user/gallery.html',{"gallery":gdata})


def contactus(req):
    status=False
    if req.method=='POST':
        Name = req.POST.get("name","")
        Email = req.POST.get("email","")
        Mobile = req.POST.get("mobile","")
        Address = req.POST.get("address","")
        Message = req.POST.get("msg","")
        res=contact(name=Name,email=Email,contact=Mobile,address=Address,message=Message)
        res.save()
        status=True
    return render(req,'user/contactus.html',{'s':status})

def viewdetails(req):
    a=req.GET.get('msg')
    data=addplace.objects.filter(id=a)
    return render(req,'user/viewdetails.html',{"d":data})

def guiderdetails(req):
    city = cities.objects.all().order_by('-id')
    a = req.GET.get('abc')
    gd = ""
    if a is None:
        gd = guider.objects.all().order_by('-id')
    else:
        gd = guider.objects.filter(city=a)
    mydict = {"city": city, "guider": gd}
    return render(req,'user/guiderdetails.html',mydict)

def newplaces(req):
    city=cities.objects.all().order_by('-id')
    place=addplace.objects.all().order_by('-id')
    a=req.GET.get('abc')
    place=""
    if a is None:
        place=addplace.objects.all().order_by('-id')
    else:
        place=addplace.objects.filter(city=a)

    mydict={"city":city,"place":place}
    return render(req,'user/newplaces.html',mydict)

def signin(req):
    return render(req,'user/signin.html')

def videogallery(req):
    vdata=video.objects.all().order_by('-id')
    return render(req,'user/video.html',{"video":vdata})



