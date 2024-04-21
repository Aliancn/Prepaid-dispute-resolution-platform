# Generated by Django 4.2.9 on 2024-04-17 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0015_rename_chatmessage_chatitem_chatrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='email',
        ),
        migrations.AddField(
            model_name='documents',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provements',
            name='document',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.documents'),
            preserve_default=False,
        ),
    ]