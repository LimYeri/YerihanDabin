# Generated by Django 4.1.3 on 2022-12-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medicine", "0005_alter_medicine_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicine",
            name="medicineImg",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
