from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, product_success

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/<int:id>/', ProductShowView.as_view(), name='show'), 
    path("products/create/", ProductCreateView.as_view(), name="create_product"),
    path("products/success/", product_success, name="product_success"),  
]
