from django import template
from django.template.loader import get_template

register = template.Library()


@register.simple_tag
def django_files_head(tag):
    files = {
        'fine-uploader-ui-gallery': 'files/fine_uploader_ui_gallery.html',
        'fine-uploader-ui-row': 'files/fine_uploader_ui_row.html',
    }

    template = get_template(files[tag])
    context = {}
    return template.render(context)


@register.simple_tag
def django_files_scripts(tag):
    files = {
        'fine-uploader-s3-core': 'files/fine-uploader/s3.fine-uploader/s3.fine-uploader.core.min.js',
        'fine-uploader-s3-ui': 'files/fine-uploader/s3.fine-uploader/s3.fine-uploader.min.js',
    }

    script = files[tag]

    template = get_template('files/django_files_scripts.html')
    context = {
        'script': script
    }
    return template.render(context)
