# Generated by Django 4.2.1 on 2023-05-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoryregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='category')),
            ],
        ),
    ]
