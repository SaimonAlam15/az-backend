# Generated by Django 5.0.3 on 2024-03-19 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options_alter_user_table"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
    ]
