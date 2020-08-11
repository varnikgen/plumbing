from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:pk>/', views.CartAddView.as_view(), name='cart_add'),
    path('remove/<int:pk>/', views.cart_remove, name='cart_remove'),
]
