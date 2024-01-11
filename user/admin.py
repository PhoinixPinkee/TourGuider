from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display=("name","contact","email","address","message")
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=('id',"cname","cpic","cdate")
admin.site.register(category,categoryAdmin)

class loginAdmin(admin.ModelAdmin):
    list_display=("name",'mobile','email','passwd',"pic","address")
admin.site.register(login,loginAdmin)

class citiesAdmin(admin.ModelAdmin):
    list_display=("id","cname","cpic","cdate")
admin.site.register(cities,citiesAdmin)

class addplaceAdmin(admin.ModelAdmin):
    list_display=('id',"ptitle","city","baplace","pdes","placepic","pdate")
admin.site.register(addplace,addplaceAdmin)

class guiderAdmin(admin.ModelAdmin):
    list_display=("name",'city','gid','gidp','qualification','guiderpic','address','gdate','mobile')
admin.site.register(guider,guiderAdmin)

class galleryAdmin(admin.ModelAdmin):
    list_display=("pdes","picture","gdate")
admin.site.register(gallery,galleryAdmin)

class videoAdmin(admin.ModelAdmin):
    list_display=("id","vtitle","vdes","thumb","vlink","vdate")
admin.site.register(video,videoAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display=("id","stitle","sdes","spic","sdate")
admin.site.register(slider,sliderAdmin)






