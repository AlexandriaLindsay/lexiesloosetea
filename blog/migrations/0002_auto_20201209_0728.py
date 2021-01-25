# Generated by Django 3.1.3 on 2020-12-09 13:28

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='custom_title',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bloglistingpage',
            name='custom_title',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
