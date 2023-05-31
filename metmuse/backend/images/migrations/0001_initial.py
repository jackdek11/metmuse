# Generated by Django 4.2.1 on 2023-05-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blacklist",
            fields=[
                (
                    "ref",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "ref",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("url", models.URLField()),
                ("name", models.TextField(blank=True, null=True)),
                ("artistDisplayName", models.TextField(blank=True, null=True)),
                ("artistDisplayBio", models.TextField(blank=True, null=True)),
                ("artistNationality", models.TextField(blank=True, null=True)),
                ("country", models.TextField(blank=True, null=True)),
                ("region", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
