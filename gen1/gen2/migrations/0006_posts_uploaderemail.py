# Generated by Django 4.2.4 on 2024-01-30 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen2', '0005_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='uploaderemail',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
    ]
