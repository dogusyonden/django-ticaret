# Generated by Django 4.2.2 on 2023-08-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0003_alter_shopcard_totalprice_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcard',
            name='stock',
            field=models.IntegerField(default=0, null=True, verbose_name='Ürün Stok'),
        ),
    ]
