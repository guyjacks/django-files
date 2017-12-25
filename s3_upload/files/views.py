from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
import json, boto3


def sign_s3(data):
    # boto3 expects the IAM credentials to be set in an environment variable
    s3 = boto3.client('s3', region_name='us-east-2')

    # Get file information
    bucket = data['conditions'][1]['bucket']
    key = data['conditions'][5]['key']

    # I don't think we're supposed to send the date with the request.
    # It causes errors sometimes when we do, but not all of the time.
    # https://github.com/aws/aws-sdk-js/issues/1514
    conditions_without_amz_date = [c for c in data['conditions'] if 'x-amz-date' not in c]

    presigned_post = s3.generate_presigned_post(
        Bucket = bucket,
        Key = key,
        Conditions = conditions_without_amz_date,
    )

    return {
        'signature': presigned_post['fields']['x-amz-signature'],
        'policy': presigned_post['fields']['policy']
    }


class S3SignatureView(APIView):

    # as an installable django plugin, how would I make authentication optional?
    # how do I allow the user to specify that the file should be related to multiple objects?
    # - register (model=Organization, field=logo, reverse=organization)
    # - register (model=Badge, field=images, reverse=badges, lookup_by=('field 1', 'field 2'))
    # - lookup_by is optional and covers cases when the related object has a multi-field primary key (default is 'pk')
    # post data will expect an optional 'related' field with the model name i.e. 'Badge' and the necessary lookup fields)

    def post(self, request, format=None):
        # how will i tell it to relate the new file to another model?
        print('/s3/signature/', request.data)
        signature = sign_s3(request.data)
        return Response(signature)


class S3SuccessView(APIView):

    def post(self, request, format=None):
        print('/s3/success/', request.data)
        return Response({})


class S3GalleryDemoView(TemplateView):
    template_name = 'files/s3_gallery_demo.html'


class S3CoreDemoView(TemplateView):
    template_name = 'files/s3_core_demo.html'
