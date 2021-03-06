"""tweety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets 
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

# A way to serialize and show users
#class UserSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = User
        #fields = ('url', 'username', 'email', 'is_staff')

#class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet) # Not using right now 

urlpatterns = [
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^users/$', views.UserList.as_view()), 
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

#Don't necessarily need to add these extra url patterns in,
#but it give us a simple, clean way of referring to a specific format
urlpatterns = format_suffix_patterns(urlpatterns)
