# Generated by Django 3.2 on 2022-03-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grow', '0002_auto_20220317_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userregistrationmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
