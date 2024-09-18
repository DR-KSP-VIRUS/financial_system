from django.urls import path

from . import views as v

app_name = 'accounts'

urlpatterns = [
    path('login', v.user_login_form, name='login'),
    path('signup', v.signup, name='signup'),
    path('logout', v.user_logout, name='logout'),
    path('dashboard', v.user_dashboard, name='dashboard'),
]