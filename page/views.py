from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.core.exceptions import ValidationError

from django.core.validators import validate_email
from django.urls import reverse






def home(request):

   if request.method == "POST":
      username = request.POST["username"]
      email = request.POST["mail"]
      phone_number = request.POST["contact"]
      text_area = request.POST["textarea"]

      if  len(email)> 0:
         try:
            validate_email(email)
      
         
         except ValidationError:
               messages.info(request, "email is invalid")
               return redirect("/#contact")
   
      if User.objects.filter(username=username).exists():
        messages.info(request, "Username already exists")
        return redirect("/#contact")

      elif not username:
         messages.info(request, "username is required")
         return redirect("/#contact") 
     
      elif len(phone_number) > 0 and len(phone_number) != 11:
         messages.info(request, "Wrong phone number")
         return redirect("/#contact")
      
      elif len(text_area) == 0:
         messages.info(request, "Text area is empty")
         return redirect("/#contact")
      
      else:
         user = User.objects.create_user(username=username, email=email, first_name=text_area)
         user.save()
       
        
         url = "/next_page" + "/" + f"{username}"
         return redirect(url)
   
   return render(request, "home.html")

   
def next_page(request, pk):
   username = User.objects.get(username = pk)
   return render(request, "next_page.html", {"username":username})
