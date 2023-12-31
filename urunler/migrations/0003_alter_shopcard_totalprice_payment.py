# Generated by Django 4.2.2 on 2023-07-27 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('urunler', '0002_alter_product_options_shopcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcard',
            name='totalPrice',
            field=models.IntegerField(editable=False, verbose_name='Toplam Fiyat'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPrice', models.IntegerField(verbose_name='Toplam Fiyat')),
                ('isPayment', models.BooleanField(default=False, verbose_name='Ödendi mi?')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Satın Alan')),
                ('products', models.ManyToManyField(to='urunler.shopcard', verbose_name='Satın Alınan Ürünler')),
            ],
        ),
    ]
