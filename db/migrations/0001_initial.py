# Generated by Django 4.1.7 on 2023-03-15 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), ('CSBS', 'Computer Science and Business Systems'), ('MBA', 'Master of Business Administration'), ('AIDS', 'Artificial Intelligence and Data Science'), ('CCE', 'Computer Science and Communication Engineering'), ('IT', 'Information Technology')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('ID', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=100)),
                ('College', models.EmailField(max_length=100)),
                ('Event', models.CharField(max_length=100)),
                ('Datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
