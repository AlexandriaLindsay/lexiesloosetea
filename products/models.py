from django.db import models
from django import forms
from django.shortcuts import render
from wagtail.search import index
from wagtail.search.backends import get_search_backend
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.fields import RichTextField

from wagtail.core import blocks
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route


# Create your models here.
class ProductListingPage(RoutablePageMixin, Page):
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = ProductDetailPage.objects.live().public().order_by('-first_published_at')
        context["categories"] = ProductCategory.objects.all()
        context["moods"] = ProductMood.objects.all()
        return context
    
    """Re Route page if a category is selected"""
    @route(r'^category/(?P<cat_slug>[-\w]*)/$', name="category_view")
    def category_view(self, request, cat_slug):

        context = self.get_context(request)

        try:
            category = ProductCategory.objects.get(slug=cat_slug)
        except expression:
            category = None
        
        if category is None:
            #Redirect to Shop
            pass

        context['posts'] = ProductDetailPage.objects.filter(categories__in=[category])
        return render(request, "products/product_listing_page.html", context)
    
    """Re Route page if a Mood is selected"""
    @route(r'^mood/(?P<cat_slug>[-\w]*)/$', name="mood_view")
    def mood_view(self, request, cat_slug):

        context = self.get_context(request)

        try:
            mood = ProductMood.objects.get(slug=cat_slug)
        except expression:
            mood = None
        
        if mood is None:
            #Redirect to Shop
            pass

        context['posts'] = ProductDetailPage.objects.filter(moods__in=[mood])
        return render(request, "products/product_listing_page.html", context)

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='Pick a Category',
    ) 

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ["name"]
    
    def __str__(self):
        return self.name

register_snippet(ProductCategory)


class ProductMood(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='Pick a Mood',
    ) 

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Product Mood"
        verbose_name_plural = "Product Moods"
        ordering = ["name"]
    
    def __str__(self):
        return self.name

register_snippet(ProductMood)


class ProductDetailPage(Page):
    description = RichTextField(blank=True)
    price = RichTextField(blank=True)

    product_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    categories = ParentalManyToManyField("products.ProductCategory", blank="True")
    moods = ParentalManyToManyField("products.ProductMood", blank="True")


    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('price'),

        ImageChooserPanel('product_image'),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        ),

        MultiFieldPanel(
            [
                FieldPanel("moods", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Moods"
        ),
    ]
