from django.urls import path
from . import views

urlpatterns = [
    path("createbook/",views.createbook,name='create'),
    path("author/",views.Create_Author, name='author'),
    path("",views.listbook,name='dash'),
    path('detailview/<int:bookid>/',views.detailview,name='detail'),# here name is used for giving link for button
    path('updateview/<int:bookid>/',views.updateview,name='update'),
    path('deleteview/<int:bookid>',views.deleteview,name='delete'),
    path('index/',views.index),
    path('search/',views.serach,name='search'),
    # path('register/',views.register,name='register'),
    # path('login/',views.login,name="login"),
    path('logout/',views.logout,name='logout'),
    path('home/',views.Homepage,name='home')

]