# Generated by Django 4.1.3 on 2022-11-29 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("medicine", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="medicine",
            old_name="contents",
            new_name="content",
        ),
    ]
