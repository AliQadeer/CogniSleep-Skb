# Generated by Django 2.2.5 on 2019-10-28 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_sleepdiary_week_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleepdiary',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
