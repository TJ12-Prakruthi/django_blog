from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
  # both are having same name as views so we gave the alias as 'auth_views'

#login view is already designed by django

urlpatterns = [
    path('sign_up/',views.sign_up,name = 'users-sign-up'),
    path('profile/',views.profile,name = 'users-profile'),
    path('',auth_views.LoginView.as_view(template_name = 'users/login.html'), name='users-login'),  # these are class based views by django we need to deal with it differently
    path('logout/',views.custom_logout, name='users-logout'),  # these are class based views by django we need to deal with it differently
    
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name = 'users-password-reset'),

    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), 
         name = 'users-password-reset-done'),
    
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), 
         name = 'users-password-reset-confirm'),
    
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), 
         name = 'users-password-reset-complete'),
    
  

]
