# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
from django_hosts.resolvers import reverse
from django.db import models

reload(sys)
sys.setdefaultencoding('utf-8')


class BaseModel(models.Model):
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        # 定义抽象类,用它来归纳一些公共属性字段
        abstract = True


class Article(BaseModel):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    status = models.CharField('状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True, help_text="")
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True)

    def get_absolute_url(self):
        return reverse('article', args=[self.id], host='blog')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category(BaseModel):
    name = models.CharField('类名', max_length=20)
    order = models.PositiveIntegerField('顺序', default=0)

    def get_absolute_url(self):
        return reverse('category', args=[self.id], host='blog')

    def __unicode__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField('标签名', max_length=20)

    def get_absolute_url(self):
        return reverse('tag', args=[self.id], host='blog')

    def __unicode__(self):
        return self.name
