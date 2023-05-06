from django.urls import include, path
from rest_framework import routers
from cart import views

router = routers.DefaultRouter()
router.register(r'cart', views.CartViewSet, basename='cart')

urlpatterns = [
    path('', include((router.urls, 'flower_shop.cart'))),
    path('user/register/', views.RegisterUser.as_view(), name='user_register'),
    path('user/login/', views.LoginUser.as_view()),
]
