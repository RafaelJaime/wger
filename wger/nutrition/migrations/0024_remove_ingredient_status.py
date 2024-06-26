# Generated by Django 4.2.13 on 2024-05-24 17:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('nutrition', '0023_fiber_spelling'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='status',
        ),
        migrations.AlterField(
            model_name='image',
            name='license_author',
            field=models.TextField(
                blank=True,
                help_text='If you are not the author, enter the name or source here.',
                max_length=3500,
                null=True,
                verbose_name='Author(s)',
            ),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fiber',
            field=models.DecimalField(
                blank=True,
                decimal_places=3,
                help_text='In g per 100g of product',
                max_digits=6,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
                verbose_name='Fiber',
            ),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='license_author',
            field=models.TextField(
                blank=True,
                help_text='If you are not the author, enter the name or source here.',
                max_length=3500,
                null=True,
                verbose_name='Author(s)',
            ),
        ),
    ]
