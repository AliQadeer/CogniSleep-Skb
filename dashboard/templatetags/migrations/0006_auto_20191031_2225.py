# Generated by Django 2.2.5 on 2019-10-31 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20191031_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleepdiary',
            name='time_fell_asleep',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sleepdiary',
            name='time_got_up',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sleepdiary',
            name='time_went_to_bed',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
