"""
URL configuration for project6 project.

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
from northfood.views import *
from southfood.views import *
from centeralfood.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nfood/',nfood,name='nfood'),
    path('food1/',food1,name='food1'),
    path('cfood/',cfood,name='cfood'),
    path('food2/',food2,name='food2'),
    path('sfood/',sfood,name='sfood'),
    path('food3/',food3,name='food3'),
]
