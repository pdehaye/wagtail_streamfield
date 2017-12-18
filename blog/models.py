# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from datetime import date

from django import forms
from django.db import models

from django.http import Http404, HttpResponse

from django.utils.dateformat import DateFormat
from django.utils.formats import date_format

import wagtail

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager

from taggit.models import TaggedItemBase, Tag as TaggitTag

from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route


class BlogPage(RoutablePageMixin, Page):
    stream_body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
    date = models.DateTimeField(verbose_name="Post date", default=datetime.datetime.today)

    content_panels = Page.content_panels + [
        StreamFieldPanel('stream_body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        context['blog_page'] = self
        return context

class PostPage(Page):
    stream_body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
    date = models.DateTimeField(verbose_name="Post date", default=datetime.datetime.today)
    # categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    # tags = ClusterTaggableManager(through='blog.BlogPageTag', blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('stream_body'),
        # FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        # FieldPanel('tags'),
    ]

    @property
    def blog_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(PostPage, self).get_context(request, *args, **kwargs)
        context['blog_page'] = self.blog_page
        context['post'] = self
        return context

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('PostPage', related_name='post_tags')

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
