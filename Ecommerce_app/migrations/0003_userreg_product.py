# Generated by Django 4.2.1 on 2023-05-26 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0002_categoryregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=250)),
                ('Phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='product')),
                ('P_description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('categoryname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce_app.categoryregister')),
            ],
        ),
    ]