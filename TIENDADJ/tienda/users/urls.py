from django.urls import path, include
from . import views
urlpatterns = [
    path('login/',views.LoginUser.as_view(),name='user_login'),
    path('api/google-login/',views.GoogleLoginView.as_view(),name='google_login'),
]