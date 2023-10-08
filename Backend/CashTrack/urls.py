"""
URL configuration for CashTrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as CustomUserView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/create/', CustomUserView.create_my_CustomUser, name='create_my_CustomUser'),
    path('user/findall/', CustomUserView.get_all_my_CustomUsers, name='get_my_CustomUser'),
    path('user/findbyid/<int:CustomUser_id>/', CustomUserView.get_CustomUser_by_id, name='get_CustomUser_by_id'),
    path('user/update/<int:pk>/', CustomUserView.update_my_CustomUser, name='update_my_CustomUser'),
    path('user/delete/<int:pk>/', CustomUserView.delete_my_CustomUser, name='delete_my_CustomUser'),
    path('user/login/', CustomUserView.login_custom_user, name='login_my_CustomUser'),
    path('user/deleteall/', CustomUserView.delete_all_CustomUsers, name='delete_all_CustomUser')
]
