# Generated by Django 5.1.7 on 2025-03-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animais',
            name='nivel_extincao',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='animais',
            name='nivel_perigo',
            field=models.CharField(max_length=100),
        ),
    ]
