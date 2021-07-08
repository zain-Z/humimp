# views

from .models import StoriesDetail
from .serializers import StoriesDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def stories_api(request):
    all_jobs = StoriesDetail.objects.all()
    data = StoriesDetailSerializer(all_stories, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def story_detail_api(request, id):
    story_detail_detail = StoriesDetail.objects.get(id=id)
    data = StoriesDetailSerializer(career_detail).data
    return Response({'data': data})


class StoriesDetailListApi(generics.ListAPIView):
    queryset = StoriesDetail.objects.all()
    serializer_class = StoriesDetailSerializer


class StoriesDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoriesDetailSerializer
    queryset = StoriesDetail.objects.all()
    lookup_field = 'id'
