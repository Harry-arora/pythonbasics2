from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


from rest_framework.decorators import api_view

from apps.crud.models import Tutorial
from apps.crud.serializers import Tutorialserializer


@api_view(['POST'])
def hello(request):
    if request.method == 'POST':
       tutorial_data = JSONParser().parse(request)
       tutorial_serializer = Tutorialserializer(data=tutorial_data)
       if tutorial_serializer.is_valid():
          tutorial_serializer.save()
        return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   # return JsonResponse({"data": "123"}, safe=False)

def hey(request):
    return JsonResponse({"hey how are you": "fine bro"}, safe=False)


@api_view(['GET'])
def single_project(request, pk):
    # ... tutorial = Tutorial.objects.get(pk=pk)

    if request.method == 'GET':
        tutorial_serializer = Tutorialserializer(Tutorial)
        return JsonResponse(tutorial_serializer.data)

    # Create your views here.


@api_view(['DELETE'])
def tutorial_delete(request):

    if request.method == 'DELETE':
    count = Tutorial.objects.all().delete()
    return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)

    if request.method == 'GET':
        tutorials_serializer = Tutorialserializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


@api_view(['PUT'])
def tutorial_put(request, pk):

    if request.method == 'PUT':
    tutorial_data = JSONParser().parse(request)
    tutorial_serializer = Tutorialserializer(Tutorial, data=tutorial_data)
    if tutorial_serializer.is_valid():
        tutorial_serializer.save()
        return JsonResponse(tutorial_serializer.data)
    return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)