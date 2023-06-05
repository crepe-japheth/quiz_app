# Generated by Django 4.1.4 on 2023-04-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='can_choose_many',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='img',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
