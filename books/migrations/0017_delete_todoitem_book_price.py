# Generated by Django 4.2.3 on 2023-10-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_todoitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TodoItem',
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
