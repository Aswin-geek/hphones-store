# Generated by Django 4.2.5 on 2023-11-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hps', '0029_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=5)),
            ],
        ),
    ]
