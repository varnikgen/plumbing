from django.urls import path

from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.ProductsView.as_view(), name="product_list"),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review"),
]
