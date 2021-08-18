from django.urls import path
from.import views
urlpatterns = [
    path('',views.index), 
    path('regform',views.regform),
    path('staff',views.stflogin),
    path('orders',views.order),
    path('menu',views.menu),
    path('offer',views.offer),
]
