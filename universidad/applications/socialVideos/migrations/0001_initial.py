# Generated by Django 4.2.3 on 2024-10-20 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_video', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
