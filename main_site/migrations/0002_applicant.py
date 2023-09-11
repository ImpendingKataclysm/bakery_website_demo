# Generated by Django 4.2.5 on 2023-09-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_available', models.DateField()),
                ('resume', models.FileField(upload_to='resumes/<django.db.models.fields.CharField>_<django.db.models.fields.CharField>.pdf')),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]