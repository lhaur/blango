# Generated by Django 3.2.5 on 2024-02-15 08:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20240215_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]