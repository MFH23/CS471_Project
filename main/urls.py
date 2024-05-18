from django.urls import path
from . import views


urlpatterns = [
    path('', views.home ,name="main-home" ),
    path('contact/', views.contact ,name="main-contact" ),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
   # path('make/', views.make_appointment, name='make_appointment'),
    #path('success/', views.appointment_success, name='appointment_success'),


    path('create/', views.create_appointment, name='create_appointment'),
    path('update/<int:pk>/', views.update_appointment, name='update_appointment'),
    path('detail/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('view', views.appointment_list, name='appointment_list'),
    path('delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
]