# Generated by Django 3.1.3 on 2020-11-24 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201124_0712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='productIntro',
            new_name='product_intro',
        ),
    ]
