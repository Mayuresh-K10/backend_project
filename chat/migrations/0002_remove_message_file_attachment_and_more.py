# Generated by Django 5.1.2 on 2024-11-21 10:21

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='file_attachment',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver_type',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender_type',
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OnlineStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_online', models.BooleanField(default=False)),
                ('last_seen', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='online_status', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
