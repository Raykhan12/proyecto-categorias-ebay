# Generated by Django 4.0 on 2022-01-02 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categorias_Ebay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CategoryName',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
