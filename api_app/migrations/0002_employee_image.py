# Generated by Django 3.2.9 on 2021-11-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
