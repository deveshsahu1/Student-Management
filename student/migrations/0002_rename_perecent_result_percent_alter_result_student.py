# Generated by Django 4.0.6 on 2022-08-05 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='perecent',
            new_name='percent',
        ),
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
