# Generated by Django 4.2.5 on 2023-10-11 06:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hps', '0012_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tot_amount', models.FloatField()),
                ('status', models.CharField(default='New Order', max_length=20)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 10, 11, 12, 26, 20, 500627))),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_method', models.CharField(max_length=20)),
                ('status', models.BooleanField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hps.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('sub_tot', models.FloatField()),
                ('status', models.CharField(default='Order Placed', max_length=20)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hps.prdvariation')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='new_order',
            field=models.ManyToManyField(to='hps.orderitem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
