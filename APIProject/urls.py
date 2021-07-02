from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from APIApp import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'address', views.AddressViewSet)

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/',obtain_auth_token)
]