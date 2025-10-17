from django.urls import path

from . import views

urlpatterns = [
    # pk is the kwarg
    path('', views.product_create_view),
    path('<int:pk>/', views.product_detail_view),  # is the same with path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    
]
