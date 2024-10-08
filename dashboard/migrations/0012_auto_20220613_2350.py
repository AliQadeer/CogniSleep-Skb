# Generated by Django 3.2 on 2022-06-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20220607_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='sleepdiary',
            name='awake_during_night',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='awake_too_early',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='delayed_getting_up',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='problem_falling_asleep',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='sleep_efficiency',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='time_in_bed',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='sleepdiary',
            name='total_sleep_time',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
