# Generated by Django 4.1.5 on 2023-03-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_media_comment_contactdetail_is_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetail',
            name='qrcode',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
