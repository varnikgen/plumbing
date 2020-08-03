from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductsView.as_view()),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review"),
]
