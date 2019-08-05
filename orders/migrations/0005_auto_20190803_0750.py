# Generated by Django 2.2.4 on 2019-08-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinnerplatter',
            name='type',
            field=models.CharField(choices=[('small', 'Small'), ('large', 'Large')], default='small', max_length=20),
        ),
        migrations.AddField(
            model_name='regularpizza',
            name='type',
            field=models.CharField(choices=[('small', 'Small'), ('large', 'Large')], default='small', max_length=20),
        ),
        migrations.AddField(
            model_name='sicilianpizza',
            name='type',
            field=models.CharField(choices=[('small', 'Small'), ('large', 'Large')], default='small', max_length=20),
        ),
        migrations.AddField(
            model_name='sub',
            name='type',
            field=models.CharField(choices=[('small', 'Small'), ('large', 'Large')], default='small', max_length=20),
        ),
        migrations.AddField(
            model_name='subaddon',
            name='type',
            field=models.CharField(choices=[('small', 'Small'), ('large', 'Large')], default='small', max_length=20),
        ),
    ]