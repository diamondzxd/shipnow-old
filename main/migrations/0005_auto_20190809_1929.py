# Generated by Django 2.2.2 on 2019-08-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_order_is_pending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
