# Generated by Django 4.2.5 on 2023-11-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hps', '0031_order_coupon_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
