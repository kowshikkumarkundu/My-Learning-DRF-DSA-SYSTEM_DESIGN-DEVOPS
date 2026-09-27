from django.urls import path
from .views import Products,ProductDetail

urlpatterns = [
    path('products/',Products.as_view()),

    path('product/<int:pk>/',ProductDetail.as_view())
]
