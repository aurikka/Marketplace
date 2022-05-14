# Generated by Django 3.2.6 on 2021-09-26 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'goods',
            },
        ),
        migrations.CreateModel(
            name='ItemPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('in_stock', models.PositiveIntegerField(default=0, verbose_name='in_stock')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_goods.item')),
            ],
            options={
                'verbose_name': 'price',
                'verbose_name_plural': 'prices',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='date of purchase')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='customer')),
            ],
            options={
                'verbose_name': 'purchase',
                'verbose_name_plural': 'purchases',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('address', models.CharField(max_length=150, verbose_name='address')),
                ('items', models.ManyToManyField(through='app_goods.ItemPrice', to='app_goods.Item', verbose_name='items')),
            ],
            options={
                'verbose_name': 'shop',
                'verbose_name_plural': 'shops',
            },
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app_goods.purchase', verbose_name='order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app_goods.item', verbose_name='product')),
            ],
        ),
        migrations.AddField(
            model_name='itemprice',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_goods.shop'),
        ),
    ]
