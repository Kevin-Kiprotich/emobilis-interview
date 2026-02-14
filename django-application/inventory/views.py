from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer
# Create your views here.
class ProductsView(APIView):
    """
    This performs CRUD operations on Products. 
    """
    def get(self, request, pk=None):
        """
        This returns all the items in the Products menu based on a query
        
        :param request: contains request information
        :param pk: primary key
        """
        if pk is None:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
        else:
            try:
                queryset = Product.objects.get(id=pk)
                serializer = ProductSerializer(queryset)
            except Product.DoesNotExist:
                return Response({"detail":"Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def put(self, request, pk=None):
        """
        This updates data inside the Products model for a single product
        
        :param request: contains request information
        :param pk: primary key
        """
        if pk is None:
            return Response({"detail":"Product id not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"detail":"Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        """
        This deletes an item in the Product model based by the item's primary key
        
        :param request: contains request information
        :param pk: primary key
        """
        if pk is None:
            return Response({"detail":"Product id not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response({"detail":"Product deleted"})
        except Product.DoesNotExist:
            return Response({"detail":"Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        """
        Docstring for post
        
        :param request: Contains the request information
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
def product_list(request):
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request, 'product_list.html',context=context)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, "product_form.html", {"form":form})
    
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    
    return render(request, "product_form.html", {"form":form})

def product_delete(request, pk):
    product=get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    
    return render(request, "product_delete.html",{"product":product})




@csrf_exempt
def stk_push(request):
    data = json.loads(request.body)
    phone = data.get("phone")
    amount = data.get("amount")

    # Call Daraja STK Push here
    # (Use your consumer key & secret)

    return JsonResponse({
        "message": "STK Push Sent Successfully"
    })
