# Generated by Django 4.1.7 on 2023-03-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ElevatorApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="elevator",
            name="destinations",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
