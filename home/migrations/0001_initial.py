# Generated by Django 2.0.1 on 2021-11-23 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254, verbose_name='郵件信箱')),
                ('website', models.URLField(default='')),
                ('phone', models.CharField(default=0, max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
            ],
            managers=[
                ('london', django.db.models.manager.Manager()),
            ],
        ),
    ]
