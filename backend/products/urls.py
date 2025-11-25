from django.urls import path

from . import views

urlpatterns = [
    # pk is the kwarg
    path('', views.product_list_create_view, name='product-list'),
    # path('', views.product_mixin_view),
    path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),  # is the same with path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    # path('<int:pk>/', views.product_mixin_view),  # is the same with path('<int:pk>/', views.ProductDetailAPIView.as_view()),

    # only for test the view
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view)
    
]
