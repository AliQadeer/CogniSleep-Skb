# Generated by Django 2.2.2 on 2019-07-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_passwordstr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='driving_license_back_img',
            field=models.ImageField(default='default.png', upload_to='user_pics'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='driving_license_front_img',
            field=models.ImageField(default='default.png', upload_to='user_pics'),
        ),
    ]
