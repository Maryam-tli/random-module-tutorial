# Generated by Django 4.2.19 on 2025-02-09 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_teaching', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['published']},
        ),
    ]
