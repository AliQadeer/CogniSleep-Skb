# Generated by Django 2.2.2 on 2019-08-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_verifiedcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verifiedcode',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
