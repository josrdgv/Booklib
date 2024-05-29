from django.urls import path
from . import views

urlpatterns = [

    path("",views.userlistbook,name='booklist'),
    path('detailview/<int:bookid>/',views.userdetailview,name='detail'),# here name is used for giving link for button
    path('search/',views.userserach,name='search'),
    path('add_to_cart/<int:bookid>',views.add_to_cart,name='addtocart'),
    path('cartview/',views.view_cart,name='cartview'),
    path('increase/<int:item_id>',views.increase_quantity,name='increase_quantity'),
    path('decrease/<int:item_id>', views.decrease_quantity, name='decrease_quantity'),
    path('remove/<int:item_id>',views.remove_item,name='remove_cart'),
    path('create_checkout_session/',views.create_checkout_session,name='create_checkout_session'),
    path('success/',views.success,name='success'),
    path('cancel/', views.cancel, name='cancel')

]