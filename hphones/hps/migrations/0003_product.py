# Generated by Django 4.2.5 on 2023-09-24 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hps', '0002_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_name', models.CharField(max_length=20)),
                ('stock', models.IntegerField()),
                ('cur_price', models.FloatField()),
                ('max_price', models.FloatField()),
                ('desc', models.CharField(max_length=50)),
                ('p_img', models.ImageField(upload_to='images')),
                ('brd_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hps.brand')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hps.category')),
            ],
        ),
    ]
