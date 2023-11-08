from cms.models.pluginmodel import CMSPlugin
from tinymce.models import HTMLField
from django.db import models


class NewsPlogin(CMSPlugin):
    title = models.CharField(max_length=50, default="title")
    body = HTMLField()
