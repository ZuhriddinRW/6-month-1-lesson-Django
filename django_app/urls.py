from django.urls import path
from . import views
from .views import add_news

urlpatterns = [
    path ( '', views.index, name='index' ),
    path ( 'categories', views.categories, name='categories' ),
    path ( 'categories/<int:category_id>/', views.categories_with_id, name='categories_by_id' ),
    path ( 'products', views.products, name='products' ),
    path ( 'products/<int:category_id>/', views.products_by_category, name='products_by_category' ),
    path ( 'suppliers', views.suppliers, name='suppliers' ),
    path ( 'add_news/', add_news, name = "add_news" )
]