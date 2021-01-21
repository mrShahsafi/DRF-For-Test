from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import SingleProductSerializer
from .models import (
            Product,
            Category,
            SubCategory
            )

#HTTP messages
SUCCESS = status.HTTP_200_OK
METHOD_NOT_ALLOWED = status.HTTP_403_FORBIDDEN
#PERMISSION_DENIED = status.HTTP_403_PERMISSION_DENIED
NOT_FOUND = status.HTTP_404_NOT_FOUND
SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR

class SingleProductApi(APIView):
    def get(self, request,id):
        product = Product.objects.filter(pk=id)
        if product:
            '''for c in product:
                category = c.category.all()'''
            serialized_data = SingleProductSerializer(
                                            product,many=True
                                                )
            data  = serialized_data.data
            '''def get_subcategory(Category):
                for a in category:
                    return a.sub_category.name'''
            return Response(
                {
                'product':data
                }
                ,
                status=SUCCESS
                )

        else:
            return Response(
                    {
                    'status':'File your looking for not found'
                    }
                    ,
                    status=NOT_FOUND
                )
    def post(self, request):
        return Response(
            {
                'status':'method not allowed'
            }
            ,
            status=METHOD_NOT_ALLOWED
            )
