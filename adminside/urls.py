from re import template
from sre_constants import SUCCESS
from django.urls import path
from app import views as appview
from adminside import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    
    path('customerview',appview.customerview,name='customerview'),
    
    path('adminprofile',views.adminprofile, name='adminprofile'),
    
    path('admindetails',views.admindetails, name='admindetails'),
    
    path('adminregistration/',views.adminregistration, name='adminregistration'),
    path('adminlogin/',views.adminlogin, name='adminlogin'),
    path('adminaddproduct/',views.adminaddproduct, name='adminaddproduct'),
    path('adminlogout/',views.adminlogout, name='adminlogout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)