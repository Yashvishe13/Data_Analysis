# Generated by Django 3.2 on 2022-03-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('cost_price', models.IntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_age', models.IntegerField()),
                ('customer_gender', models.CharField(max_length=100)),
            ],
        ),
    ]
