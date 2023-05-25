from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post

def home(request):

    name_error_message = ""
    text_area_error_message=""
    name_value=""
    text_area_value=""
    pop_up_name=""
    
    
    if request.method == "POST":
        name = request.POST['name']
        mail=request.POST["mail"]
        contact=request.POST['contact']
        textarea=request.POST['texrarea']
       

        name_len= len(str(name))
        text_area=len(str(textarea))

        if name_len < 1:
            name_error_message= "This field is required"

        if name_len >= 1:
            name_value=name
        
        if text_area < 1:
            text_area_error_message= "This field is required"

        if text_area >= 1:
            text_area_value=textarea

        if name_len >= 1 and text_area >= 1:
            text_area_value=""
            name_value=""
            pop_up_name=name
            messages.info(request, "k")
            a = Post.objects.create(name=name,textarea=textarea)
            a.save()
        
    return render(request, "home.html", {"pop_up_name":pop_up_name, "name_error_message":name_error_message, "text_area_error_message":text_area_error_message,"name":name_value, "textarea":text_area_value})
