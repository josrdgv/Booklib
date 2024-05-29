from django.contrib import auth
from django.core.mail import message
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render,redirect
from .form import Authorform,Bookform
# Create your views here.
from .models import Book,Author
from django.contrib.auth.models import User

####################################### Normally we are using like this ##################################
# def createbook(request):
#     books = Book.objects.all()  # for printing the value in the same page
#
#     if request.method=="POST":
#
#
#         title=request.POST.get('title')
#         # we use this to retrive the value from html using name 'title' that is specified in the bracket
#
#
#         price=request.POST.get('price')
#         # we use this to retrive the value from html using name 'title' that is specified in the bracket
#
#
#         book=Book(title=title,price=price)
#         #Book is the model name,red title is the title that is specified in the model.py and white title is used to connect the details from html page
#         #same for the case of price
#         book.save()
#     # return render(request,'book.html')
#     return render(request, 'book.html',{"books":books}) # this render is used for render in the same page
#
#

# to view the stored results we have use another method
#if we want to view the stored in the same page


#this will view the results in listbook.html so we have to create listbook.html
# Note

# whenever we create a function in view we have to create a url inthe urls.py



#to print a specific element with id



#toupdate a detail

# def updateview(request,bookid):
#     book=Book.objects.get(id=bookid)
#
#     if request.method=="POST":
#
#
#       title=request.POST.get('title')
#       price=request.POST.get('price')
#       book.title=title
#       book.price=price
#
#       book.save()
#         #to return to home page
#       return redirect('/')
#
#     return render(request,'updateview.html',{'book':book})
#

# to delete an element

def deleteview(request,bookid):
    book=Book.objects.get(id=bookid)
    if request.method=="POST":
        book.delete()
        return redirect('/')
    return render(request,"manager/deleteview.html",{'book':book})







############################################# When using form  #####################################################

def createbook(request):
    books=Book.objects.all()

    if request.method=='POST':
        form=Bookform(request.POST,request.FILES)

        print(form)

        if form.is_valid(): #checking whether the form is valid
            form.save()

            return redirect('/')
    else:
        form=Bookform()
    return render(request,'manager/book.html' ,{'form':form,'books':books})


def Create_Author(request):

    if request.method=="POST":
        form=Authorform(request.POST)
        print(form)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form=Authorform()
    return render(request,'manager/author.html',{'form':form})

def updateview(request,bookid):
    books=Book.objects.get(id=bookid)

    if request.method=="POST":
        form=Bookform(request.POST,request.FILES,instance=books)     #instance is used to identify which model is used

        if form.is_valid():
            form.save()
            return redirect('/')
    else:

        form=Bookform(instance=books)
    return render(request,'manager/updateview.html',{'form':form})


def index(request):
    return render(request,'manager/index.html')




# def register(request):
#
#     if request.method=='POST':
#         username=request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpassword')
#
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 message.info(request,'this username is already exist')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 message.info(request,'this Mail is already exist')
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
#                 user.save()
#                 return redirect('login')
#         else:
#             message.info(request,'the password is not matching')
#             return redirect('register')
#     return render(request,'register.html')
#
#
# def login(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('home')
#         else:
#             message.info(request,'Please provide correct information')
#             return redirect('login')
#
#
#     return render(request,'login.html')

def logout(request):
    auth.logout()
    return redirect('login')

def listbook(request):
    books=Book.objects.all()


    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page('page_number')

    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request, 'manager/listbook.html', {"books": books, 'page': page})


def detailview(request,bookid): #here bookid is passed to print specific element from database
    book=Book.objects.get(id=bookid)#to get the corresponding id
    return render(request,'manager/detailview.html',{'book':book})

def serach(request):

    query=None
    book=None


    if 'q' in request.GET:

        query =request.GET.get('q')
        book=Book.objects.filter(Q(title__icontains=query))
    else:
        book=[]
    return render(request,'manager/search.html',{'book':book,'query':query})
def Homepage(request):
    return render(request,'manager/home.html')