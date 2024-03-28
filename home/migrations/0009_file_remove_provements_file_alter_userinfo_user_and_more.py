
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_alter_userinfo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('intro', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='static/files/')),
            ],
        ),
        migrations.RemoveField(
            model_name='provements',
            name='file',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='provements',
            name='file_provements',
            field=models.ManyToManyField(related_name='file_provements', to='home.file'),
        ),
    ]
