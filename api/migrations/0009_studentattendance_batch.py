# Generated by Django 5.1.1 on 2024-09-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_attendancerecord_location_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattendance',
            name='batch',
            field=models.CharField(default='G1', max_length=100),
            preserve_default=False,
        ),
    ]