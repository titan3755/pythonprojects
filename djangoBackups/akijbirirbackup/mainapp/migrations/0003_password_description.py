# Generated by Django 3.2 on 2021-05-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_password_logged_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]