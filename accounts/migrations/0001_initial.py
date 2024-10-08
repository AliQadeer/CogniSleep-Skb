# Generated by Django 2.2.2 on 2019-07-17 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('first_login', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('isprovider', models.BooleanField(default=False)),
                ('isverified', models.BooleanField(default=False)),
                ('packageno', models.BooleanField(default=False)),
                ('verifiedcode', models.CharField(max_length=20)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=20)),
                ('license_state', models.CharField(max_length=20)),
                ('type_of_practice', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('practice_name', models.CharField(max_length=50)),
                ('practice_phone_number', models.CharField(max_length=20)),
                ('practice_address', models.CharField(max_length=200)),
                ('driving_license_front_img', models.CharField(max_length=100)),
                ('driving_license_back_img', models.CharField(max_length=100)),
                ('fax_no', models.CharField(max_length=20)),
                ('primary_care_office_name', models.CharField(max_length=100)),
                ('primary_care_doctor_name', models.CharField(max_length=100)),
                ('doctor_ref_number', models.CharField(max_length=20)),
                ('is_provider', models.BooleanField(default=False)),
                ('patient_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
