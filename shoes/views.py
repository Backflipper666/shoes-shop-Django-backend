#views.py
from django.http import JsonResponse
from .models import Shoe, User
from .serializers import ShoeSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.static import serve
from django.http import HttpResponse

def my_view(request):
    image_name = request.GET.get('image_name')
    if image_name is None:
        print('Oh noooooooooooooooooooooooooo')
        return HttpResponse('No image name was passed')

    image_path = '/static/images/{}'.format(image_name)
    return serve(request, image_path)


@api_view(['GET', 'POST'])
def shoe_list(request):
    if request.method == 'GET':
        shoes = Shoe.objects.all()
        serializer = ShoeSerializer(shoes, many=True)
        return JsonResponse({"shoes":serializer.data},)
    elif request.method == 'POST':
        serializer = ShoeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({"users":serializer.data},)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def shoes_detail(request, id):
    try:
        shoe = Shoe.objects.get(pk=id)
    except Shoe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShoeSerializer(shoe)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ShoeSerializer(shoe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        shoe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
