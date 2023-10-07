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
from CashTrackApp.views import AccountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/create/', AccountView.create_my_account, name='create_my_account'),
    path('account/findall/', AccountView.get_all_my_accounts, name='get_my_account'),
    path('account/findbyid/<int:account_id>/', AccountView.get_account_by_id, name='get_account_by_id'),
    path('account/update/<int:pk>/', AccountView.update_my_account, name='update_my_account'),
    path('account/delete/<int:pk>/', AccountView.delete_my_account, name='delete_my_account'),


]
