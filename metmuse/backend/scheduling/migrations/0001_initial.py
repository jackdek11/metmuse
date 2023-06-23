# Generated by Django 4.2.2 on 2023-06-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FetchableImages",
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
                ("object_id", models.IntegerField()),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "This image still needs to be fetched"),
                            (2, "This image is busy being fetched"),
                            (3, "This image was fetched correctly"),
                            (4, "There was an error while fetching this image"),
                        ],
                        default=1,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Fetchable Images",
                "db_table": "metmuse.fetchable_images",
            },
        ),
    ]
