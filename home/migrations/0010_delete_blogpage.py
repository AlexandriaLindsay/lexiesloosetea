# Generated by Django 3.1.3 on 2020-12-07 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0009_aboutpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPage',
        ),
    ]
