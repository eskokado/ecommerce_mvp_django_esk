from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path("api/", include("categories.urls")),
    path("api/", include("products.urls")),
    path("api/", include("carts.urls")),
    path("api/", include("orders.urls"))
]
