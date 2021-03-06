# Generated by Django 4.0.2 on 2022-02-13 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_gift'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftset',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giftset',
            name='image',
            field=models.CharField(default=str, max_length=250),
        ),
        migrations.AddField(
            model_name='giftset',
            name='verified_gift',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='giftset',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
