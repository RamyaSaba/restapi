from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token
from api import views
from django.urls import path


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
]