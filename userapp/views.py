from django.conf import settings
from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.urls import reverse

# Create your views here.
from bookapp.models import Book,Author

from django.contrib.auth.models import User
from .models import Cart,cartitem
import stripe


# Create your views here.

def userlistbook(request):
    books=Book.objects.all()


    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page('page_number')

    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request, 'user/userlistview.html', {"books": books, 'page': page})




def userdetailview(request,bookid): #here bookid is passed to print specific element from database
    book=Book.objects.get(id=bookid)#to get the corresponding id
    return render(request,'user/userdetail.html',{'book':book})

def userserach(request):

    query=None
    book=None


    if 'q' in request.GET:

        query =request.GET.get('q')
        book=Book.objects.filter(Q(title__icontains=query))
    else:
        book=[]
    return render(request,'user/usersearch.html',{'book':book,'query':query})


def add_to_cart(request, bookid):
    book=Book.objects.get(id=bookid)

    if book.quantity>0:
        cart,created= Cart.objects.get_or_create(user=request.user)
        cart_item,item_created=cartitem.objects.get_or_create(cart=cart,book=book)

        if not item_created:
            cart_item.quality+=1
            cart_item.save()
    return redirect('cartview')

def view_cart(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_items=cart.cartitem_set.all()
    cart_item=cartitem.objects.all()
    total_price=sum(items.book.price * items.quantity for items in cart_items)
    total_items=cart_items.count()

    context={'cart_items':cart_items,'cart_item':cart_item,'total_price':total_price,'total_items':total_items}
    return render(request,'user/cart.html',context)

def increase_quantity(request,item_id):
    cart_item=cartitem.objects.get(id=item_id)
    if cart_item.quantity < cart_item.book.quantity:
        cart_item.quatity+=1
        cart_item.save()
    return redirect('cartview')

def decrease_quantity(request,item_id):
    cart_item=cartitem.objects.get(id=item_id)
    if cart_item.quatity >1:
        cart_item.quatity-=1
        cart_item.save()
    return redirect('cartview')

def remove_item(request,item_id):
    try:

       cart_item = cartitem.objects.get(id=item_id)
       cart_item.delete()
    except cart_item.DoesNotExist:
        pass
    return redirect('cartview')

def create_checkout_session(request):
    cart_item=cartitem.objects.all()

    if cart_item:
        stripe.api_key=settings.STRIPE_SECRET_KEY

        if request.method=='POST':

            line_items=[]
            for cart_items in cart_item:
                if cart_items.book:

                    line_item={
                        'price_data':{
                            'currency':'INR',
                            'unit_amount':int(cart_items.book.price * 100),
                            'product_data':{
                                'name':cart_items.book.title

                            },
                        },
                        'quantity':1
                    }
                    line_items.append(line_item)
            if line_items:

                checkout_session=stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    success_url=request.build_absolute_uri(reverse('success')),
                    cancel_url=request.build_absolute_uri(reverse('cancel'))
                )
                return redirect(checkout_session.url,code=303)



def success(request):
    cart_item=cartitem.objects.all()

    for cart_items in cart_item:
        product=cart_items.book

        if product.quantity >= cart_items.quantity:
            product.quantity-=cart_items.quantity
            product.save()
    cart_item.delete()
    return render(request,'user/success.html')

def cancel(request):
    return render(request,'user/cancel.html')


