# Generated by Django 2.2.5 on 2019-12-05 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='member',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chat'),
        ),
        migrations.AddField(
            model_name='member',
            name='last_read_message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chats.Message'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Chat', to='chats.Message'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chats.Chat'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Message'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
