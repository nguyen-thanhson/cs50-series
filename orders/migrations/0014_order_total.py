# Generated by Django 2.2.4 on 2019-08-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20190805_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
