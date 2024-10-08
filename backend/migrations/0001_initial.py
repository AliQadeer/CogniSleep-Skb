# Generated by Django 3.2 on 2022-07-20 18:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptionpackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('package_name', models.CharField(max_length=80, null=True)),
                ('no_free_months', models.IntegerField(default=0)),
                ('no_discounted_months', models.IntegerField(default=0)),
                ('discounted_price', models.IntegerField(default=0)),
                ('base_price', models.IntegerField(default=0)),
                ('package_detail', models.CharField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'subscription_package',
            },
        ),
    ]
