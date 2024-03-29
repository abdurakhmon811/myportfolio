# Generated by Django 4.1.5 on 2023-04-14 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('knowledge_extent', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('Native', 'Native')], max_length=20)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(max_length=100)),
                ('media_image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('started', models.DateField()),
                ('still_learning', models.BooleanField(default=True)),
                ('ended', models.DateField(null=True)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_created', models.CharField(choices=[('My own', 'My own'), ('With team', 'With team')], max_length=100, null=True)),
                ('project_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='images')),
                ('date_finished', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_place', models.CharField(max_length=150)),
                ('as_a', models.CharField(max_length=150)),
                ('started', models.DateField()),
                ('still_working', models.BooleanField(default=False)),
                ('ended', models.DateField()),
                ('comment', models.TextField()),
                ('employment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.worktype')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=150)),
                ('faculty', models.CharField(max_length=150)),
                ('major', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('still_studying', models.BooleanField(default=False)),
                ('end_date', models.DateField(null=True)),
                ('comment', models.TextField(null=True)),
                ('education', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.educationdegree')),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000, null=True)),
                ('comment', models.TextField(null=True)),
                ('is_url', models.BooleanField(default=False)),
                ('is_email', models.BooleanField(default=False)),
                ('is_phone_number', models.BooleanField(default=False)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.media')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(null=True, upload_to='images')),
                ('title', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('full_bio', models.TextField()),
                ('short_bio', models.TextField(null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('hobbies', models.CharField(max_length=100, null=True)),
                ('resume_link', models.URLField(null=True)),
                ('education', models.ManyToManyField(to='main.education')),
                ('languages', models.ManyToManyField(to='main.language')),
                ('programming_languages', models.ManyToManyField(to='main.programminglanguage')),
                ('work_experience', models.ManyToManyField(to='main.workexperience')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
    ]
