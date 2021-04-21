from django.urls import path, include
from . import views
from rest_framework.authtoken import views as views_token


urlpatterns = [
    path('api/', views.MapView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.locator),
    path('api_token_auth/', views_token.obtain_auth_token, name='auth-token'),
]