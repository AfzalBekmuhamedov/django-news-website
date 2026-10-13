from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(),name="home"),
    path('signup/', SignUp.as_view(),name="signup"),
    path('search/', Search.as_view(), name="search"),
    path('signin/', SignIn.as_view(), name="signin"),
    path('signout/', SignOut.as_view(), name="signout"),
    path('articles/<int:pk>/', Detail.as_view(), name="detail"),
    path('categories/<int:pk>/', Category.as_view(), name="category"),
    path('comments/<int:pk>/', AddComment.as_view(), name="comment"),
]