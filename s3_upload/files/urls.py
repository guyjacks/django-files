from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import S3SignatureView, S3SuccessView, S3CoreDemoView, S3GalleryDemoView, S3RowDemoView

urlpatterns = [
    url(r'^s3/signature/$', S3SignatureView.as_view()),
    url(r'^s3/success/$', S3SuccessView.as_view()),
    url(r'^files/demo/s3-row/$', S3RowDemoView.as_view()),
    url(r'^files/demo/s3-gallery/$', S3GalleryDemoView.as_view()),
    url(r'^files/demo/s3-core/$', S3CoreDemoView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
