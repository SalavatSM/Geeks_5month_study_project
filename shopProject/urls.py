from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test_api_view),
    path('api/v1/products/', views.product_list_api_view),
    path('api/v1/products/<int:id>/', views.product_item_api_view)
]

#  API - Application Programming Interface
