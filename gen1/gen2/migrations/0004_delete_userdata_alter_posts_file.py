# Generated by Django 4.2.4 on 2024-01-30 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen2', '0003_posts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserData',
        ),
        migrations.AlterField(
            model_name='posts',
            name='file',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
