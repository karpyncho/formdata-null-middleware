from django.urls import path
from django.http import HttpResponse


def my_view(request):
    html = "<html><body>Hello World</body></html>"
    return HttpResponse(html)


urlpatterns = [path('hello/', my_view, name='hello'), ]
