# Generated by Django 2.2.7 on 2020-08-16 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_auto_20200814_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='likes',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.Post'),
        ),
    ]
