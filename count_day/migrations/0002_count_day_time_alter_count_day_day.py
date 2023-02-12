# Generated by Django 4.1.6 on 2023-02-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("count_day", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="count_day",
            name="Time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="count_day",
            name="day",
            field=models.DateField(default=0),
            preserve_default=False,
        ),
    ]
