from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *

# Create your views here.
def regform(request):
    if request.method=='POST':
        try:
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            email=request.POST['email']
            username=request.POST['username']
            pass_word=request.POST['password']
            login=Login_staff(user_name=username,password=pass_word)
            login.save()
            person=Registrationform(first_name=firstname,last_name=lastname,email=email,login=login)
            person.save()
            return render(request,'registrationform.html',{'msg':'registered succesfully'})
        except Exception as error:
            return render(request,'registrationform.html',{'msg':error})
      
    else:
        return render(request,'registrationform.html')
    

def stflogin(request):
  if request.method=='POST':
    try:
      username=request.POST['username']
      password=request.POST['password']
      log_obj=Login_staff.objects.get(user_name=username,password=password)
      return render(request,'order.html')
    except Exception as error:
      return render(request,'stafflogin.html',{'msg':'please enter valid details'})
  return render(request,'stafflogin.html')
def order(request):
    return render(request,'order.html')    
def menu(request):
  return render(request,'menu.html')
def offer(request):
  if request.method=='POST':
    try:
      item=request.POST['food']
      price=request.POST['price']
      offer=request.POST['offer']
      special=Todays_special(food_item=item,price=price,discount=offer)
      special.save()
      print(special)
    except Exception as error:
      return render(request,'special.html',{'msg1':'error'})
  return render(request,'special.html')

def index(request):
  if request.method=='POST':
    try:
      username=request.POST['username']
      tablenumber=request.POST['tableno']
      customer=Login_customer(customer_name=username,table_no=tablenumber)
      customer.save()
      return render(request,'menu.html')
    except Exception as error:
      return render(request,'index.html',{'msg':'check details you entered are correct'})
  return render(request,'index.html')  
  
 
  

 