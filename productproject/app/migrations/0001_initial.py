# Generated by Django 5.1.7 on 2025-03-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
                ("subcategory", models.CharField(max_length=50)),
                ("price", models.FloatField()),
            ],
        ),
    ]
