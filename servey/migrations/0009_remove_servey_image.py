# Generated by Django 4.1.6 on 2023-02-08 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("servey", "0008_alter_servey_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servey",
            name="image",
        ),
    ]
