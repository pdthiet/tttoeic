from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.shortcuts import get_object_or_404 

# Create your views here.
@api_view(['GET'])
def get_all_vip_price(request):
    try:
        vips = VipPrice.objects.all()
        serializer = GetAllVipPriceSerializer(vips, many=True)
        return Response(serializer.data)
    except VipPrice.DoesNotExist:
        return Response({"detail": "No data VipPrice."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def get_all_vip_function(request):
    try:
        vips = VipFunction.objects.all()
        serializer = GetAllVipFunctionSerializer(vips, many=True)
        return Response(serializer.data)
    except VipFunction.DoesNotExist:
        return Response({"detail": "No data."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['PUT'])
def update_vip_price(request):
    id = request.GET['id']
    try:
        vipPrice = VipPrice.objects.get(id=id)
    except VipPrice.DoesNotExist:
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UpdateVipPriceSerializer(vipPrice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_vip_price(request):
    id = request.GET['id']
    try:
        vipPrice = VipPrice.objects.get(id=id)
    except VipPrice.DoesNotExist:
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        vipPrice.delete()
        return Response({"message": "Xóa thành công"}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def create_vip_price(request):
    if request.method == 'POST':
        serializer = CreateVipPriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

