# Generated by Django 5.0.6 on 2024-07-12 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amt',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
