# Generated by Django 4.1.7 on 2023-03-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Elevator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("current_floor", models.IntegerField(default=1)),
                ("destinations", models.JSONField(default=list)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("start", "START"),
                            ("stop", "STOP"),
                            ("not_working", "NOT WORKING"),
                        ],
                        default="stop",
                        max_length=20,
                    ),
                ),
                (
                    "direction",
                    models.CharField(
                        choices=[("up", "UP"), ("down", "DOWN"), ("idle", "IDLE")],
                        default="idle",
                        max_length=4,
                    ),
                ),
                (
                    "door",
                    models.CharField(
                        choices=[("open", "OPEN"), ("close", "CLOSE")],
                        default="close",
                        max_length=5,
                    ),
                ),
            ],
        ),
    ]
