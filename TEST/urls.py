from django.urls import path
from api.views import ProductListCreate, ProductDetail, RegisterView, LoginView

urlpatterns = [
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<str:product_id>/', ProductDetail.as_view(), name='product-detail'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
]
