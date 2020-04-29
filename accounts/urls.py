from django.urls import path
from .import views
# Create your views here.
urlpatterns = [
    path('register',views.reg,name="register"),
    path('login',views.log,name="login"),
    path('logout',views.logout,name="logout"),

    
]
