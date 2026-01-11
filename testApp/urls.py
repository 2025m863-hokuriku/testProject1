from django.urls import path
from . import views
from .views import PostListAPIView

urlpatterns = [
    path('api/posts/', PostListAPIView.as_view()),
]