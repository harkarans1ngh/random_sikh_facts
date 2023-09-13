# Generated by Django 4.2.3 on 2023-07-20 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("facts", "0003_rename_facts_fact"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="activefact",
            name="retrieved_at",
        ),
        migrations.AddField(
            model_name="fact",
            name="retrieved_at",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
