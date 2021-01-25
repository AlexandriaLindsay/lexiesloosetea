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
class BlogListingPage(RoutablePageMixin, Page):


    ajax_template = "blog/blog_listing_page_ajax.html"

    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public().order_by('-first_published_at')
        context["categories"] = BlogCategory.objects.all()
        return context

    @route(r'^latest/$', name="latest_posts")
    def lastest_blog_posts(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['latest_posts'] = BlogDetailPage.objects.live().public()[:1]
        return render(request, "blog/latest_posts.html", context)

    """Re Route page if a category is selected"""
    @route(r'^category/(?P<cat_slug>[-\w]*)/$', name="category_view")
    def category_view(self, request, cat_slug):

        context = self.get_context(request)

        try:
            category = BlogCategory.objects.get(slug=cat_slug)
        except expression:
            category = None
        
        if category is None:
            #Redirect to blog
            pass

        context['posts'] = BlogDetailPage.objects.filter(categories__in=[category])
        return render(request, "blog/blog_listing_page.html", context)



class BlogCategory(models.Model):
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
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    

register_snippet(BlogCategory)


class BlogDetailPage(Page):
    description = RichTextField(blank=True)

    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    categories = ParentalManyToManyField("blog.BlogCategory", blank="True")

 

    # content = StreamField(
    #     [
    #         ("title_and_text", blocks.TitleAndTextBlock()),
    #         ("full_richtext", blocks.RichTextBlock()),
    #         ("simple_richtext", blocks.SimpleRichTextBlock()),
    #         ("cards", blocks.CardBlock()),
    #         ("cta", blocks.CTABlock()),
    #     ],
    #     null=True,
    #     blank=True,
    # )
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        ImageChooserPanel('blog_image'),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        ),
    ]
    