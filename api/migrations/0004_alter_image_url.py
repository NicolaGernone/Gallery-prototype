# Generated by Django 4.1 on 2022-09-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_image_grid_alter_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
