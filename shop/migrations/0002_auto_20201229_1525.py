# Generated by Django 3.1.4 on 2020-12-29 09:25

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='handle',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
    ]
