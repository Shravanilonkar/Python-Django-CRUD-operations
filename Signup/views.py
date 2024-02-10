from django.shortcuts import render, redirect
from .models import Customer

# Create your views here.
def Signup(request):
    return render(request,"Signup.html")

def insertData(request):
    data=Customer.objects.all()
    context={"data":data}
    if request.method=="POST":
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        print(uname,email,password,cpassword)
        query=Customer(uname=uname,email=email,password=password,cpassword=cpassword)
        query.save()
    return render(request,"SignupInformation.html",context)

def updateData(request,email):
    if request.method=="POST":
        uname=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        edit=Customer.objects.get(email=email)
        edit.uname=uname
        edit.email=email
        edit.password=password
        edit.cpassword=cpassword
        edit.save()
        return redirect("insertData")
    

    d=Customer.objects.get(email=email)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,email):
    d=Customer.objects.get(email=email)
    d.delete()
    return redirect("insertData")


