# Generated by Django 4.2.5 on 2023-11-01 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hps', '0030_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon_apply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hps.coupon'),
        ),
    ]