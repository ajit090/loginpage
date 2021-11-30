from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('expression',views.expression,name='expression')

]