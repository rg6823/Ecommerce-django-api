from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination

# Create your views here.

class CustomPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 20
    page_query_param = 'p'

    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        return response


####    PRODUCT GENERIC-API-VIEW

class ProductGenericView(GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class=PageNumberPagination
    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'), 
            'age': request.data.get('age'), 
            'category': request.data.get('category'), 
            'description': request.data.get('description'), 
            'selling_price': request.data.get('selling_price'), 
            }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductdetailGenericView(GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class=PageNumberPagination
    def get_object_with_id(self, product_id):
        return Product.objects.get(id=product_id)
    def get(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object_with_id(product_id)
        if not product_instance:
            return Response(
                {"result": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ProductSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object_with_id(product_id)
        if not product_instance:
            return Response(
                {"res": "Object with product id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        product_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    def put(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object_with_id(product_id)
        if not product_instance:
            return Response(
                {"result": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'title': request.data.get('title'), 
            'age': request.data.get('age'), 
            'category': request.data.get('category'), 
            'description': request.data.get('description'), 
            'selling_price': request.data.get('selling_price'), 
            }
        serializer = ProductSerializer(instance = product_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#   CATEGORY GENERIC-API-VIEW
class CategoryGenericView(GenericAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    pagination_class=PageNumberPagination
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        data = {
            'name':request.data.get('name'),
            }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategorydetailGenericView(GenericAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    pagination_class=PageNumberPagination

    def get_object_with_id(self, category_id):
        return Category.objects.get(id=category_id)
    def get(self, request, category_id, *args, **kwargs):
        category_instance = self.get_object_with_id(category_id)
        if not category_instance:
            return Response(
                {"result": "Object with category id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CategorySerializer(category_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, category_id, *args, **kwargs):
        category_instance = self.get_object_with_id(category_id)
        if not category_instance:
            return Response(
                {"res": "Object with category id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        category_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

    def put(self, request, category_id, *args, **kwargs):
        category_instance = self.get_object_with_id(category_id)
        if not category_instance:
            return Response(
                {"result": "Object with category id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'), 
            }
        serializer = CategorySerializer(instance = category_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   ORDER GENERIC-API-VIEW
class OrderGenericView(GenericAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    pagination_class=PageNumberPagination
    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        data = {
            'customer':request.data.get('customer'),
            'total':request.data.get('total'),
            'mobile': request.data.get('mobile'),
            'product':request.data.get('product'),
            }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderdetailGenericView(GenericAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    pagination_class=PageNumberPagination
    def get_object_with_id(self, order_id):
        return Order.objects.get(id=order_id)
    def get(self, request, order_id, *args, **kwargs):
        order_instance = self.get_object_with_id(order_id)
        if not order_instance:
            return Response(
                {"result": "Object with order id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderSerializer(order_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, order_id, *args, **kwargs):
        order_instance = self.get_object_with_id(order_id)
        if not order_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'customer':request.data.get('customer'),
            'total':request.data.get('total'),
            'mobile': request.data.get('mobile'),
            'product':request.data.get('product'),
            }
        serializer = OrderSerializer(instance = order_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, order_id, *args, **kwargs):
        order_instance = self.get_object_with_id(order_id)
        if not order_instance:
            return Response(
                {"res": "Object with order id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        order_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
#   CUSTOMER GENERIC-API-VIEW
class CustomerGenericView(GenericAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    pagination_class=PageNumberPagination
    
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        data = {
            'name':request.data.get('name'),
            'address':request.data.get('address'),
            'email': request.data.get('email'),
            }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerdetailGenericView(GenericAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    pagination_class=PageNumberPagination

    def get_object_with_id(self, customer_id):
        return Customer.objects.get(id=customer_id)
    def get(self, request, customer_id, *args, **kwargs):
        customer_instance = self.get_object_with_id(customer_id)
        if not customer_instance:
            return Response(
                {"result": "Object with customer id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CustomerSerializer(customer_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, customer_id, *args, **kwargs):
        customer_instance = self.get_object_with_id(customer_id)
        if not customer_instance:
            return Response(
                {"res": "Object with customer id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name':request.data.get('name'),
            'address':request.data.get('address'),
            'email': request.data.get('email'),
            }
        serializer = CustomerSerializer(instance = customer_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id, *args, **kwargs):
        customer_instance = self.get_object_with_id(customer_id)
        if not customer_instance:
            return Response(
                {"res": "Object with customer id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        customer_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
#   STOCK GENERIC-API-VIEW
class StockGenericView(GenericAPIView):
    queryset=Stock.objects.all()
    serializer_class=StockSerializer
    pagination_class=PageNumberPagination
    
    def get(self, request, *args, **kwargs):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        data = {
            'units': request.data.get('units'),
            'product':request.data.get('product'), 
            }
        serializer = StockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class StockdetailGenericView(GenericAPIView):
    queryset=Stock.objects.all()
    serializer_class=StockSerializer
    pagination_class=PageNumberPagination

    def get_object_with_id(self, stock_id):
        return Stock.objects.get(id=stock_id)
    def get(self, request, stock_id, *args, **kwargs):
        stock_instance = self.get_object_with_id(stock_id)
        if not stock_instance:
            return Response(
                {"result": "Object with stock id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StockSerializer(stock_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, stock_id, *args, **kwargs):
        stock_instance = self.get_object_with_id(stock_id)
        if not stock_instance:
            return Response(
                {"result": "Object with stock id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'units': request.data.get('units'),
            'product':request.data.get('product'), 
            }
        serializer = StockSerializer(instance = stock_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




## LIST CREATE APIVIEW, RETRIEVE UPDATE DESTROY APIVIEW

# from django.shortcuts import render
# from rest_framework import generics
# from .models import *
# from .serializers import *



# class ListCategory(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class ListProduct(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ListOrder(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class ListCustomer(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class DetailCustomer(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class ListStock(generics.ListCreateAPIView):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer





