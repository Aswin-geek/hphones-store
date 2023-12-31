# Generated by Django 4.2.5 on 2023-09-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hps', '0004_alter_product_p_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brd_status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='cat_status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prd_status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='warr',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
