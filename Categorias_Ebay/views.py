from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Categorias_Ebay.models import Category
from Categorias_Ebay.serializers import CategorySerializers

@csrf_exempt
def categoryApi(request,id=0):
    if request.method=='GET':
        category = Category.objects.all()
        Category_serializer = CategorySerializers(category, many=True)
        return JsonResponse(Category_serializer.data , safe=False)
        

    elif request.method=='POST':
        category_data=JSONParser().parse(request)
        Category_serializer = CategorySerializers(data=category_data)
        if Category_serializer.is_valid():
            Category_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        category_data = JSONParser().parse(request)
        category=Category.objects.get(CategoryID=category_data['CategoryID'])
        Category_serializer=CategorySerializers(category,data=category_data)
        if Category_serializer.is_valid():
            Category_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        category_data = JSONParser().parse(request)
        category=Category.objects.get(CategoryID=category_data['CategoryID'])
        category.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)