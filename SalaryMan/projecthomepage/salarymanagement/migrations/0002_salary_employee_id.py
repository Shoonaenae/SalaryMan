# Generated by Django 3.2.7 on 2021-10-23 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salarymanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='salarymanagement.employee'),
        ),
    ]
