# Generated by Django 4.1.5 on 2023-02-03 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_project_project_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(choices=[('Associate degree', 'Associate degree'), ("Bachelor's degree", "Bachelor's degree"), ("Master's degree", "Master's degree"), ('Doctoral degree', 'Doctoral degree')], max_length=100)),
                ('institution', models.CharField(max_length=150)),
                ('faculty', models.CharField(max_length=150)),
                ('major', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('still_studying', models.BooleanField(default=False)),
                ('end_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('knowledge_extent', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('Native', 'Native')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('started', models.DateField()),
                ('still_learning', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_place', models.CharField(max_length=150)),
                ('as_a', models.CharField(max_length=150)),
                ('employment_type', models.CharField(choices=[('Remote full-time', 'Remote full-time'), ('Remote part-time', 'Remote part-time'), ('Remote contract', 'Remote contract'), ('In-person full-time', 'In-person full-time'), ('In-person part-time', 'In-person part-time'), ('In-person contract', 'In-person contract'), ('Freelance', 'Freelance')], max_length=100)),
                ('started', models.DateField()),
                ('still_working', models.BooleanField(default=False)),
                ('ended', models.DateField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='hobbies',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='skills',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='education',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.education'),
        ),
        migrations.AddField(
            model_name='about',
            name='languages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.language'),
        ),
        migrations.AddField(
            model_name='about',
            name='programming_languages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.programminglanguage'),
        ),
        migrations.AddField(
            model_name='about',
            name='work_experience',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.workexperience'),
        ),
    ]
