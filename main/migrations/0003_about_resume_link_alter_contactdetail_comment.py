# Generated by Django 4.1.5 on 2023-01-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='resume_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
