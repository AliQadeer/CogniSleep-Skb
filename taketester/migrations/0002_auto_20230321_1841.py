# Generated by Django 3.2.9 on 2023-03-21 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taketester', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('is_pre', models.BooleanField(default=False)),
                ('is_post', models.BooleanField(default=False)),
                ('year', models.IntegerField()),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='taketester.options_new')),
            ],
        ),
        migrations.AddField(
            model_name='options_new',
            name='Question_new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taketester.question_new'),
        ),
    ]
