# Generated by Django 3.2 on 2022-06-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_videoviews_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='sleepdiary',
            name='desire_wakeup_time',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='lights_out',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='minutes_fall_asleep',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='minutes_fellback_sleep',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='number_of_naps',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='totlatime_napping_minutes',
            field=models.IntegerField(null=True),
        ),
    ]
