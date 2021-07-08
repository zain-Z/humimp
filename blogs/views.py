from django.shortcuts import render
from .models import Blog, StoryList, StoryAndBlog, Team, StoriesDetail
from .serializers import BlogSerializer, StoryListSerializer, StoryAndBlogSerializer, StoriesDetailSerializer, TeamSerializer
from django.http import HttpRequest
from .filters import StoriesDetailFilter
from .form import StoriesDetailForm
from django.core.paginator import Paginator


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


def stories(request):
    """Renders the create volunteer page."""
    stories = StoriesDetail.objects.all()
    assert isinstance(request, HttpRequest)
    queryset = StoryList.objects.all()
    serializer_class = StoryListSerializer(queryset, many=True)

    # filters
    myfilter = StoriesDetailFilter(request.GET, queryset=stories)
    stories = myfilter.qs

    # Show many contacts per page.
    paginator = Paginator(stories, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'stories': page_obj, 'myfilter': myfilter,
               'data': serializer_class.data}  # template name

    return render(request, 'stories.html', context)


def stories_detail(request, id):
    """Renders the create volunteer page."""
    stories = StoriesDetail.objects.get(id=id)
    assert isinstance(request, HttpRequest)
    queryset = StoriesDetail.objects.all()
    serializer_class = StoriesDetailSerializer(queryset, many=True)

    context = {'story': stories, 'data': serializer_class.data}
    return render(request, 'stories_detail.html', context)


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
