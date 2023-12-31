# Generated by Django 4.2.2 on 2023-06-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='inventory',
            new_name='no_of_guests',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='no_of_guests',
            new_name='inventory',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='price',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='booking_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
