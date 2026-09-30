from django.urls import path,include
from .views import ProductList,ProductDetail
from .concrete_generic_views import ProductList1,ProductDetail1
from rest_framework.routers import DefaultRouter
from .viewset import ProductViewSet

router = DefaultRouter()

router.register(
    "kowshik",
    ProductViewSet,
    basename="product"
)



urlpatterns = [
    path('',ProductList.as_view()),
    path('<int:pk>/',ProductDetail.as_view()),
    path('one/',ProductList1.as_view()),
    path('one/<int:pk>/',ProductDetail1.as_view()),
    path('', include(router.urls))
]
