# Generated by Django 4.0.5 on 2022-06-17 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceName', models.CharField(max_length=100)),
                ('pinNum', models.IntegerField()),
                ('topic', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='homeboardtopic',
            name='id',
        ),
        migrations.AlterField(
            model_name='homeboardtopic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
