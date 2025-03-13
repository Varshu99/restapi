from django.shortcuts import render
from .models import Product

from .serializers import ProductSerializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(["GET"])
def Apioverview(req):
    api_urls={
        "all_products":"/",
        "add_products":"/AddProduct",
        "update_product":"/UpdateProduct/update/pk",
        "delete_product":"/product/pk/delete"
    }
    return Response(api_urls)

class AllProductview(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

class AddProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers


class UpdateProduct(generics.RetrieveUpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    partial=True
