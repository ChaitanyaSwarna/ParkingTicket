# Generated by Django 3.2.13 on 2023-10-14 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_project', '0003_alter_ticket_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
