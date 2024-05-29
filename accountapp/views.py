from django.contrib.auth import logout
from django.shortcuts import render,redirect
from .models import loginuser,userReg
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def User_Reg(request):
    login_table=loginuser()
    userprofile=userReg()

    if request.method=='POST':

       userprofile.username=request.POST['username']
       userprofile.password = request.POST['password']
       userprofile.password1 = request.POST['password1']


       login_table.username = request.POST['username']
       login_table.password = request.POST['password']
       login_table.password1 = request.POST['password1']
       login_table.type='user'

       if request.POST['password']==request.POST['password1']:
           login_table.save()
           userprofile.save()
           messages.success(request,'Register Sucessfully')
           return redirect('login')
       else:
           messages.info(request,'password not matching')
           return redirect('register')
    return render(request,'register.html')



def login(request):
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']
        user=loginuser.objects.filter(username=username,password=password,type='user')
        try:
            if user is not None:


                 user_details=loginuser.objects.get(username=username,password=password)
                 user_name=user_details.username
                 type=user_details.type

                 if type=='user':
                     request.session['username']=user_name
                     return redirect('booklist')
                 elif type=='admin':
                       request.session['username'] = user_name
                       return redirect('dash')
            else:
                 messages.error(request,"Invalid username or password")
        except:
            messages.error(request,'invalid role')
    return render(request,'login.html')


#  def adminview(request):
#     user_name=request.session['username']
#     return render(request,'admin_view.html',{'user_name':user_name})
# def userview(request):
#     user_name = request.session['username']
#     return render(request,'user_view.html',{'user_name':user_name})
# def logout_view(request):
#     logout(request)
#     return redirect('login')


