# Generated by Django 4.2.5 on 2023-10-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hps', '0024_remove_wallet_created_at_remove_wallet_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
