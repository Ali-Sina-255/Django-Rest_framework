# Generated by Django 5.0.6 on 2024-07-19 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0010_alter_cart_id_alter_cartitem_cart"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="cartitem",
            unique_together={("cart", "product")},
        ),
    ]
