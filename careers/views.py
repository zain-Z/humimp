from django.shortcuts import redirect, render
from .models import CareerDetail
from django.core.paginator import Paginator
from .form import CareerDetailForm
from django.urls import reverse
from django.http import HttpRequest
from .serializers import CareerDetailSerializer
from .filters import CareerDetailFilter

# Create your views here.


def career_list(request):
    career_list = CareerDetail.objects.all()
    assert isinstance(request, HttpRequest)
    queryset = CareerDetail.objects.all()
    serializer_class = CareerDetailSerializer(queryset, many=True)

    # filters
    myfilter = CareerDetailFilter(request.GET, queryset=career_list)
    career_list = myfilter.qs

    # Show many contacts per page.
    paginator = Paginator(career_list, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'careers': page_obj, 'myfilter': myfilter}  # template name

    return render(request, 'career_list.html', context)


def career_detail(request, id):
    career_detail = CareerDetail.objects.get(id=id)
    assert isinstance(request, HttpRequest)
    queryset = CareerDetail.objects.all()
    serializer_class = CareerDetailSerializer(queryset, many=True)

    context = {'career': career_detail}
    return render(request, 'career_detail.html', context)
