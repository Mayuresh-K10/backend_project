# Generated by Django 5.1.5 on 2025-02-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0147_new_user_enquiry_collegename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iit_locations', models.CharField(max_length=50)),
                ('iiit_locations', models.CharField(max_length=50)),
                ('nit_locations', models.CharField(max_length=50)),
                ('iim_locations', models.CharField(max_length=50)),
            ],
        ),
    ]
