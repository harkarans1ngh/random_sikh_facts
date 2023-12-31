# Generated by Django 4.2.3 on 2023-07-19 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Facts",
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
                ("category", models.CharField(max_length=100, verbose_name="Category")),
                (
                    "fact_string",
                    models.CharField(max_length=2000, verbose_name="Description"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ActiveFact",
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
                ("retrieved_at", models.DateField()),
                (
                    "retrieved_fact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="facts.facts"
                    ),
                ),
            ],
            options={
                "ordering": ["retrieved_fact"],
            },
        ),
    ]
