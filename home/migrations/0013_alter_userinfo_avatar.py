# Generated by Django 4.2.9 on 2024-03-29 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_userinfo_avator_userinfo_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/avatar/'),
        ),
    ]
