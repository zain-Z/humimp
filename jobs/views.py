from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Application, WhatWeAreDoing, Volunteer, WhoWeAre, Index, Donate, WhatWeAreDoingDetails, About, GetInvolved
from .serializers import ApplicationSerializer, WhoWeAreSerializer, WhatWeAreDoingSerializer, VolunteerSerializer, IndexSerializer, DonateSerializer, WhatWeAreDoingDetailsSerializer, AboutSerializer, GetInvolvedSerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ApplicationRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
template_name = "applicantsList.html"


def applicantsList(request):
    """Renders the applicants list page."""
    assert isinstance(request, HttpRequest)
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer(queryset, many=True)

    full_name = request.GET.get('full_name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    region = request.GET.get('region')
    address = request.GET.get('address')
    gender = request.GET.get('gender')
    english = request.GET.get('english')
    arabic = request.GET.get('arabic')
    kurdish = request.GET.get('kurdish')
    cover_letter = request.GET.get('cover_letter')
    upload_cv = request.GET.get('upload_cv')

    application = Application.objects.create(full_name=full_name,
                                             email=email,
                                             phone=phone,
                                             region=region,
                                             address=address,
                                             gender=gender,
                                             english=english,
                                             arabic=arabic,
                                             kurdish=kurdish,
                                             cover_letter=cover_letter,
                                             upload_cv=upload_cv,)

    return render(request, 'applicantsList.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def what_we_are_doing(request):
    """Renders the what we are doing page."""
    assert isinstance(request, HttpRequest)
    queryset = WhatWeAreDoing.objects.all()
    serializer_class = WhatWeAreDoingSerializer(queryset, many=True)

    return render(request, 'what_we_are_doing.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def volunteer(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer(queryset, many=True)

    return render(request, 'volunteer.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def index(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Index.objects.all()
    serializer_class = IndexSerializer(queryset, many=True)

    return render(request, 'index.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def donate(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer(queryset, many=True)

    return render(request, 'donate.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def what_we_are_doing_details(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = WhatWeAreDoingDetails.objects.all()
    serializer_class = WhatWeAreDoingDetailsSerializer(queryset, many=True)

    return render(request, 'what_we_are_doing_details.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def about(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = About.objects.all()
    serializer_class = AboutSerializer(queryset, many=True)

    return render(request, 'about.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def get_involved(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = GetInvolved.objects.all()
    serializer_class = GetInvolvedSerializer(queryset, many=True)

    return render(request, 'get_involved.html',
                  {
                      'data': serializer_class.data,
                  }
                  )


def who_we_are(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = WhoWeAre.objects.all()
    serializer_class = WhoWeAreSerializer(queryset, many=True)

    return render(request, 'who_we_are.html',
                  {
                      'data': serializer_class.data,
                  }
                  )
