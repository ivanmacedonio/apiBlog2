# Generated by Django 4.2.5 on 2023-10-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]
