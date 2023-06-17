from django.shortcuts import redirect,render, HttpResponse
from app.models import Employees
from django.contrib.auth.models import User, auth
from django.contrib import messages

# def home(request):
#     return render(request, 'home.html')



def INDEX(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp
    }

    return render(request, 'index.html',context)

def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.POST.get('image')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name = name,
            email = email,
            image = image,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('home')
    
    return render(request,'index.html')

def EDIT(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp,
    }
    return redirect(request, 'index.html',context)

def Update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.POST.get('image')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id = id,
            name = name,
            email = email,
            image = image,
            address = address,
            phone = phone,
        )
        emp.save()
        return redirect('home')
    return redirect(request, 'index.html')

# def Delete(request, id):
#     emp = Employees.objects.filter(id=id)
#     emp.delete()

#     context = {
#         'emp':emp
#     }
#     return redirect(request, 'home',context)

def Delete(r,id):
    user = Employees.objects.get(id=id)
    user.delete()
    return redirect('home')

def EmployeeShow(request):
    emp=Employees.objects.all()
    return render(request,'EmployeShow.html',locals())


def Registion(request):
    if request.method == 'POST':
        first_name=request.POST.get('frist_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        Email=request.POST.get('Email')
        Password1=request.POST.get('Password1')
        
        Password2=request.POST.get('Password2')
        
        
        if Password1 == Password2: 
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User name is already taken.')
                return redirect(Registion)
            elif User.objects.filter(email=Email).exists():
                messages.error(request, 'Email is already taken.')
                return redirect(Registion)
            else:
                user_obj = User.objects.create(first_name=first_name, last_name=last_name, username=username  ,email=Email, password=Password1)
                user_obj.set_password(Password1)
                user_obj.save()
                messages.warning(request, 'Please check in your email, and verify your account.')
            return redirect(Login)
        else:
            messages.error(request,'password and conforim password not match ')
            return redirect(Registion)
       
                 
        

    return render(request,'Regisation.html')   

def Login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.error(request,'user is not found ')
            return redirect(Login)
        else:
            auth.login(request,user)
            if user.is_superuser:
                messages.success(request,'user Login successfully')
                return redirect(INDEX)      
            else:
                messages.success(request,'user Login successfully')
                return redirect(EmployeeShow)
                     
    return render(request,'Login.html')
