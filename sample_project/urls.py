"""sample_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from main.views import *
from .serializers import CustomJWTSerializer
from rest_framework_jwt.views import obtain_jwt_token, ObtainJSONWebToken
from user.views import *
from .views import *
from django.conf import settings 
from django.conf.urls.static import static
#from .views import ObtainJSONWebToken
urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', CategoryListAPIView.as_view(), name='category'),
    path('category/add/', CategoryCreateAPIView.as_view(), name='category_add'),
    path('category/<int:pk>', CategoryRetrieveAPIView.as_view(), name='category_get'),
    path('category/update/<int:pk>', CategoryUpdateAPIView.as_view(), name='cat_update'),
    path('category/delete/<int:pk>', CategoryDestroyAPIView.as_view(), name='cat_del'),
    path('user/register/', UserCreateAPIView.as_view(), name='register'),
    path('api/token/', CustomObtainAuthToken.as_view()),
    
#    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
