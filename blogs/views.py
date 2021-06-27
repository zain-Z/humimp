from django.shortcuts import render
from .models import Blog, Story, StoryAndBlog, Team, StoriesDetail
from .serializers import BlogSerializer, StorySerializer, StoryAndBlogSerializer, StoriesDetailSerializer, TeamSerializer
from django.http import HttpRequest


def blogs(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer(queryset, many=True)

    return render(request, 'blogs.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def story(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Story.objects.all()
    serializer_class = StorySerializer(queryset, many=True)

    return render(request, 'stories.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def stories_and_blogs(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = StoryAndBlog.objects.all()
    serializer_class = StoryAndBlogSerializer(queryset, many=True)

    return render(request, 'StoriesAndBlogs.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def teams(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer(queryset, many=True)

    return render(request, 'teams.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def stories_detail(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = StoriesDetail.objects.all()
    serializer_class = StoriesDetailSerializer(queryset, many=True)

    return render(request, 'stories_detail.html',
                  {
                      'data': serializer_class.data,
                  }
                  )
