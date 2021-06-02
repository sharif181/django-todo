from django.urls import path 
from . import views

urlpatterns = [
    path('',views.userLogin,name='login'),
    path('signup',views.userSignUp,name='signup'),
    path('logout',views.userLogout,name="logout"),
    path('index',views.index,name='index'),
    path('delete/<int:pk>',views.deleteTask,name='delete_task')
]