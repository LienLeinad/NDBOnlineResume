from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    template = "home/marketing-index.html"
