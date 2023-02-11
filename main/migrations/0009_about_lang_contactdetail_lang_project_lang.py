# Generated by Django 4.1.5 on 2023-02-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_education_language_programminglanguage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='lang',
            field=models.CharField(choices=[('en', 'en'), ('ru', 'ru'), ('uz', 'uz')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='lang',
            field=models.CharField(choices=[('en', 'en'), ('ru', 'ru'), ('uz', 'uz')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='lang',
            field=models.CharField(choices=[('en', 'en'), ('ru', 'ru'), ('uz', 'uz')], max_length=2, null=True),
        ),
    ]
