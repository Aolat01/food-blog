"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from myshopInfinity.views import signin, shoplist, editmyshop, deleteMyshop, handleComplete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),

    path('',TemplateView.as_view(template_name= 'index.html'), name='home'),
    path("add-payment/", TemplateView.as_view(template_name ="addpayment.html"), name = 'add-payment'),
    path("signIn", signin , name='signIn'),
    path("YourList", shoplist , name='YourList'),
    path("edit-myshop/<int:myshop_id>/", editmyshop, name='edit-myshop'),
    path("delete-myshop/<int:myshop_id>/" , deleteMyshop, name = 'delete-myshop'),
    path("handle-complete/<int:myshop_id>/" ,handleComplete, name = 'handle-complete'),
    path("product/", include("productApp.urls")),
    path("aboutme/", TemplateView.as_view(template_name ="aboutme.html"), name = 'aboutme'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("userApp/", include("userApp.urls")),
    path("tipspage/", TemplateView.as_view(template_name ="tipspage.html"), name = 'tipspage'),
    path("recipePost/", TemplateView.as_view(template_name ="recipePost.html"), name = 'recipePost'),



]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)