# Generated by Django 4.1.5 on 2023-03-02 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contactdetail_qrcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdetail',
            name='qrcode',
        ),
    ]
