from django.urls import path
from . import views
urlpatterns = [

    path('register/',views.User_Reg,name='register'),
    path('',views.login,name='login'),
    # path('adminview/',views.adminview,name='adminview'),
    # path('userview/',views.userview,name='userview'),
    # path('logout/',views.logout_view,name='logout')
]