# Generated by Django 2.2.5 on 2019-11-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20191118_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='driving_license_back_img',
            field=models.ImageField(default='/media/default.png', upload_to='user_pics'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='driving_license_front_img',
            field=models.ImageField(default='/media/default.png', upload_to='user_pics'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='provider_image',
            field=models.ImageField(default='/media/default.png', upload_to='user_pics'),
        ),
    ]
