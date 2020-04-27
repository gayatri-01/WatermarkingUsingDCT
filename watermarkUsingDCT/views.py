from django.shortcuts import render,redirect
from django.http import HttpResponse
from .water import watermarkImage
from django.conf.urls.static import static
import os
from .forms import *
from django.conf import settings
# Create your views here.


   
  
# # Importing Image module from PIL package  
# from PIL import Image  
# import PIL  
  
# # creating a image object (main image)  
# im1 = Image.open(r"C:\Users\System-Pc\Desktop\flower1.jpg")  
  
# # save a image using extension 
# im1 = im1.save("geeks.jpg")
# im = Image.open(StringIO(request.FILES['im'].read()))


# v

def index(request):
    if request.method == 'POST': 
        form = WaterMarkForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            watermarkImage("test")            
            return render(request, 'index.html', {'form' : form, "success":True,"processed":False,"embed":False,"recovered":False}) 
    else: 
        form = WaterMarkForm() 
    return render(request, 'index.html', {'form' : form, "success":False,"processed":False,"embed":False,"recovered":False}) 

def success(request): 
    watermarkImage("test")
    return HttpResponse('successfully uploaded')  

def process(request):
         
    form = WaterMarkForm()      
    return render(request, 'index.html', {'form' : form,"success":True, "processed":True,"embed":False,"recovered":False}) 
    

def embed(request):
    form = WaterMarkForm()            
    return render(request, 'index.html', {'form' : form,"success":True, "processed":True,"embed":True,"recovered":False}) 
    
def recover(request):
    form = WaterMarkForm()        
    return render(request, 'index.html', {'form' : form,"success":True, "processed":True,"embed":True,"recovered":True}) 
    
# def uploadImages(request):
#     if request.method == "POST":
#         coverImage = request.POST.get('coverImage')     
#         wImage = request.POST.get('watermarkImage')
#         watermarkImage("test")
#         return HttpResponse(json.dumps({'status':'success'}),content_type='application/json')
        
#     else:
#         return render(request,'index.html')



  

  
  


