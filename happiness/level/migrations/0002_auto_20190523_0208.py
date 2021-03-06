# Generated by Django 2.2.1 on 2019-05-23 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('level', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='poll',
            index=models.Index(fields=['happy_level', 'date'], name='level_poll_happy_l_cd252c_idx'),
        ),
        migrations.AddIndex(
            model_name='poll',
            index=models.Index(fields=['happy_level', 'date', 'user'], name='level_poll_happy_l_81f3c9_idx'),
        ),
        migrations.AddIndex(
            model_name='poll',
            index=models.Index(fields=['happy_level'], name='level_poll_happy_l_13747a_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='poll',
            unique_together={('user', 'date')},
        ),
    ]
