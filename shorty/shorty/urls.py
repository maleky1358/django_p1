"""shorty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include
from graphene_django.views import GraphQLView
from shortener import views
from shortener.views import root
from shortener.views import home_view



urlpatterns = [
    path('', home_view ),
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.index.as_view(), name='index'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('<str:url_hash>/', root, name='root'),
    path('short/', include('shortener.urls')),
]
