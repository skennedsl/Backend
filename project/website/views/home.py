from django.http import HttpResponse
# from django.views.generic import View
from django.views.generic import TemplateView
import json

class Home(TemplateView):
    template_name = "website/index.html"