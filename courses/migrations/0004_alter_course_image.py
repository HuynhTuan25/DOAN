# Generated by Django 4.0.2 on 2022-09-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='courses/%Y/%m'),
        ),
    ]