from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^tag/(?P<tag_id>\d+)$', views.IndexView.as_view(), name='tag'),
    url(r'^category/(?P<category_id>\d+)$', views.IndexView.as_view(), name='category'),
]
