# Generated by Django 5.0.6 on 2024-07-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qurulmalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('brand_name', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='25')),
            ],
        ),
    ]