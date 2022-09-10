from django.urls import path
from . import views
from .views import edit, dashboard, register
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

app_name = 'grow'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(template_name='grow/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='grow/password_change_form.html'), name='password_change'),
    path('password_change/dond/', PasswordChangeDoneView.as_view(template_name='grow/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='grow/password_reset_form.html',
        email_template_name='grow/password_reset_email.html',
        success_url=reverse_lazy('grow:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='grow/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='grow/password_reset_confirm.html',
        success_url=reverse_lazy('grow:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='grow/password_reset_complete.html'), name='password_reset_complete'),

    path('data', views.data_entry, name='data_entry'),
    path('growabout', views.grow_about, name='grow_about'),    

]
