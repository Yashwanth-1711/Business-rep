# Generated by Django 5.1.1 on 2024-10-25 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0003_attendancemenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceMenus1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attendance_status', models.CharField(blank=True, max_length=100, null=True)),
                ('Attendance_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attendance_records', to='Business.employee')),
            ],
        ),
        migrations.DeleteModel(
            name='AttendanceMenu',
        ),
    ]
