from django.urls import path
from .views import *

urlpatterns = [
    path('category/',CategoryGenericView.as_view(), name='Categories'),
    path('category/<int:category_id>/', CategorydetailGenericView.as_view(), name='SingleCategory'),
    path('customer/', CustomerGenericView.as_view(), name = 'Customers'),
    path('customer/<int:customer_id>/', CustomerdetailGenericView.as_view(), name='SingleCustomer'),
    path('order/', OrderGenericView.as_view(), name='Orders'),
    path('order/<int:order_id>/', OrderdetailGenericView.as_view(), name='SingleOrder'),
    path('stock/',StockGenericView.as_view(), name='Stocks'),
    path('stock/<int:stock_id>/', StockdetailGenericView.as_view(), name='SingleStock'),
    path('product/', ProductGenericView.as_view(),name='Products'),
    path('product/<int:product_id>', ProductdetailGenericView.as_view(), name='SingleProduct'),
]