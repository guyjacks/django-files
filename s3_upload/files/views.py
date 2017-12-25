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
    acl = data['conditions'][0]['acl']
    file_type = data['conditions'][2]['Content-Type']

    presigned_post = s3.generate_presigned_post(
        Bucket = bucket,
        Key = key,
        Fields = {
            "acl": acl,
            "Content-Type": file_type
        },
        Conditions = data['conditions'],
    )

    return {
        'signature': presigned_post['fields']['x-amz-signature'],
        'policy': presigned_post['fields']['policy']
    }


class FileCreateView(APIView):

    # as an installable django plugin, how would I make authentication optional?
    # how do I allow the user to specify that the file should be related to multiple objects?
    # - register (model=Organization, field=logo, reverse=organization)
    # - register (model=Badge, field=images, reverse=badges, lookup_by=('field 1', 'field 2'))
    # - lookup_by is optional and covers cases when the related object has a multi-field primary key (default is 'pk')
    # post data will expect an optional 'related' field with the model name i.e. 'Badge' and the necessary lookup fields)

    def post(self, request, format=None):
        # how will i tell it to relate the new file to another model?
        print('POST', request.data)
        signature = sign_s3(request.data)
        print('signature', signature)
        return Response(signature)


class FileUpdateView(APIView):
    def put(self, request, pk, format=None):
        # update the file
        print('PUT', pk, request.data)

    def delete(self, pk):
        # delete the database record
        # delete the s3 file
        pass


class DemoView(TemplateView):
    template_name = 'files/demo.html'
