# Generated by Django 4.1.2 on 2022-12-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reseller', '0003_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='p_discription',
        ),
        migrations.AddField(
            model_name='product',
            name='p_description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
