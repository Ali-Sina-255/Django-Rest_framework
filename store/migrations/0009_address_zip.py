# Generated by Django 5.0.6 on 2024-07-17 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='1005', max_length=200),
            preserve_default=False,
        ),
    ]