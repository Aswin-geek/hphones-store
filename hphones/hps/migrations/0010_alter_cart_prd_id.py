# Generated by Django 4.2.5 on 2023-10-08 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hps', '0009_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='prd_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hps.prdvariation'),
        ),
    ]
