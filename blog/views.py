# --coding:utf-8--
import sys
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView


class IndexView(ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        pass
