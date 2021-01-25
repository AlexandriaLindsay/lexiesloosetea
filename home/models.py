from django.db import models
from products.models import ProductDetailPage
from django.shortcuts import render
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.fields import RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import ListBlock
from wagtail.core.blocks import CharBlock


from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    StreamFieldPanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)

from wagtailcaptcha.models import WagtailCaptchaEmailForm


class FormField2(AbstractFormField):
    page = ParentalKey(
        'HomePage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )



class HomePage(AbstractEmailForm, Page):
    intro = RichTextField(blank=True)
    product_intro = RichTextField(blank=True)
    popular_teas = RichTextField(blank=True)
    health_benefits = RichTextField(blank=True)

    template = "home/home_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "home/home_page.html"
    
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('product_intro', classname="full"),
        FieldPanel('popular_teas', classname="full"),
        FieldPanel('health_benefits', classname="full"),
        InlinePanel('form_fields', label='Form Fields'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = ProductDetailPage.objects.live().public().order_by('-first_published_at')
        return context
    
class AboutPage(Page):
    body = RichTextField(blank=True)
 
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )




class ContactPage(WagtailCaptchaEmailForm):
    template = "home/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "home/contact_page.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]

