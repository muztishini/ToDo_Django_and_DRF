# Generated by Django 4.2.8 on 2024-01-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0002_alter_task_status_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]