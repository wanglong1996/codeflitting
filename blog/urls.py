from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^tag/(?P<tag_id>\d+)$', views.IndexView.as_view(), name='tag'),
    url(r'^category/(?P<category_id>\d+)$', views.IndexView.as_view(), name='category'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='article'),
    url(r'^markdown/', views.MarkdownView.as_view(), name='markdown'),
]
