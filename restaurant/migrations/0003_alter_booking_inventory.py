# Generated by Django 4.2.2 on 2023-06-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_menu_no_of_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='inventory',
            field=models.IntegerField(),
        ),
    ]