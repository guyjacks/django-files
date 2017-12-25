from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FileCreateView, FileUpdateView, DemoView

urlpatterns = [
    url(r'^files/$', FileCreateView.as_view()),
    url(r'^files/(?P<pk>\d+)/$', FileUpdateView.as_view()),
    url(r'^files/demo/$', DemoView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)