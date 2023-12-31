# Generated by Django 4.2.5 on 2023-10-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hps', '0020_alter_order_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ban_img', models.FileField(upload_to='images')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
