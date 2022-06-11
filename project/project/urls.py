from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home/', views.home),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('inventory/',views.inventory,name='inventory'),
    path('product/',views.product,name='product'),
    path('analysis/',views.analysis,name='analysis'),
    path('add_supplier/',views.add_supplier,name='add_supplier'),
    path('add_sparepart/',views.add_sparepart,name='add_sparepart'),
]
