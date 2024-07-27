from django.urls import path

from website import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'), #use this if you want to create a separate login page
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'), #passes int primary key in the url, eg: url/record/1
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('add_record', views.add_record, name='add_record'),
]
