from django.urls import path
from .import views
from .import view
# Create your views here.
urlpatterns = [
    path('',views.index,name="ind"),
 
    path('search',view.search,name="sea"),
    path('sum<int:id>',views.sum,name="sumary"),
    path('according',views.acc,name="sumary"),
    path('contact',views.con,name="contact"),
    path('gallery',views.gal,name="galery"),
]
