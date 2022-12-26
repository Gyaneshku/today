from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('show/',views.show, name='show'),
    #path('delete/<int:id>/', views.delete, name='delete'),
    path('contact/',views.contact, name = 'contact'),
]