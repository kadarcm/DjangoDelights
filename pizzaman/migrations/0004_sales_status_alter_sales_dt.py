# Generated by Django 4.2.4 on 2024-01-12 03:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pizzaman", "0003_remove_saleslines_id_saleslines_line_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sales",
            name="status",
            field=models.CharField(
                choices=[
                    ("open", "o"),
                    ("closed", "c"),
                    ("canceled", "x"),
                    ("didnt pay", "r"),
                ],
                db_index=True,
                default="o",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="sales",
            name="dt",
            field=models.DateTimeField(db_index=True, default=datetime.datetime.now),
        ),
    ]