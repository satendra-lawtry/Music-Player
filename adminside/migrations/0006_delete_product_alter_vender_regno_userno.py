# Generated by Django 4.1 on 2023-01-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0005_rename_productadd_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterField(
            model_name='vender',
            name='regno_userno',
            field=models.CharField(max_length=50),
        ),
    ]