# Generated by Django 4.2.5 on 2023-09-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]