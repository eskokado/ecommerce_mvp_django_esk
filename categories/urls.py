from django.urls import path

from categories.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("categories/", CategoryListCreateAPIView.as_view(), name="categories-list-create"),
    path("categories/<int:pk>/", CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-retrieve-update-destroy"),
]
