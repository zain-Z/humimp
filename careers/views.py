from django.shortcuts import render
from .models import CareerDetail
from .serializers import CareerDetailSerializer
from django.http import HttpRequest


def careerdetail(request):
    """Renders the applicants list page."""
    assert isinstance(request, HttpRequest)
    queryset = CareerDetail.objects.all()
    serializer_class = CareerDetailSerializer(queryset, many=True)

    return render(request, 'career_details.html',
                  {
                      'data': serializer_class.data,
                  }
                  )
