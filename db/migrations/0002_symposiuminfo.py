# Generated by Django 4.1.7 on 2023-03-15 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SymposiumInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_full_name', models.CharField(max_length=255)),
                ('symp_name', models.CharField(max_length=255)),
                ('symp_date', models.DateField()),
                ('convenor', models.CharField(max_length=255)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.department')),
            ],
        ),
    ]
