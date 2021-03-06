# --coding:utf-8--
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from blog.models import Article, Category


class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        if 'category_id' in self.kwargs:
            article_list = Article.objects.filter(status='p', category=self.kwargs.get('category_id'))
        elif 'tag_id' in self.kwargs:
            article_list = Article.objects.filter(status='p', tags__in=[self.kwargs.get('tag_id')])
        else:
            article_list = Article.objects.filter(status='p')

        for article in article_list:
            article.created_time = article.created_time.strftime('%d %B %Y')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_active'] = int(self.kwargs.get('category_id', -1))
        kwargs['category_list'] = Category.objects.order_by('order')
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        article = super(ArticleDetailView, self).get_object()
        article.created_time = article.created_time.strftime('%Y-%m-%d')
        return article
