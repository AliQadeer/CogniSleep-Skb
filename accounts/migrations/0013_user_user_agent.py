# Generated by Django 2.2.5 on 2019-12-31 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20191118_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_agent',
            field=models.CharField(default='', max_length=50),
        ),
    ]
