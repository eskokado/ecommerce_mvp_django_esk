from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("categories.urls")),
    path("api/", include("products.urls")),
    path("api/", include("carts.urls")),
    path("api/", include("orders.urls"))
]
