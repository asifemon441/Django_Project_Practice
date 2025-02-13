from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('add', views.add_product, name="add_product"),
    path('update/<int:product_id>', views.update_product, name="update_product"),
    path('delete/<int:product_id>', views.delete_product, name="delete_product"),
]