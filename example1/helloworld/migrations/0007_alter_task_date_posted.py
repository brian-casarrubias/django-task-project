# Generated by Django 4.2.6 on 2023-11-28 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0006_alter_task_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
