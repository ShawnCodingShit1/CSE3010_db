from django.urls import path
from . import views

urlpatterns = [
    path('', views.toLogin_view, name='login'),
    path('login/', views.Login_view, name='authenticate'),
    path('toregister/', views.toRegister_view, name='toregister'),
    path('register/', views.Register_view, name='register'),
    # 其他URL模式
]
