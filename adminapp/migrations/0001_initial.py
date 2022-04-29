# Generated by Django 4.0.1 on 2022-04-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home_wallpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallpaper_text', models.CharField(max_length=150)),
                ('wallpaper_pic', models.ImageField(blank=True, default='-', null=True, upload_to='img', verbose_name='file')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
