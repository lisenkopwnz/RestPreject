# Generated by Django 5.1.1 on 2024-09-20 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal1', '0002_rename_category_typeanimal_animal_delete_women'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='type',
        ),
        migrations.DeleteModel(
            name='TypeAnimal',
        ),
    ]
