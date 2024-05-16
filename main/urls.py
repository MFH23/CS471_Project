from django.urls import path
from . import views


urlpatterns = [
    path('', views.home ,name="main-home" ),
    path('contact/', views.contact ,name="main-contact" ),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('make/', views.make_appointment, name='make_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),
]