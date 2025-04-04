# Generated by Django 5.1.7 on 2025-03-31 01:00

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('origin', models.CharField(choices=[('Manual', 'Manual'), ('Import', 'Import'), ('System', 'System'), ('Integration', 'Integration')], default='Manual', max_length=20, verbose_name='Origin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='Model')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='Color')),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='Brand')),
                ('engine', models.CharField(blank=True, max_length=100, null=True, verbose_name='Engine')),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic'), ('Semi-automatic', 'Semi-automatic'), ('CVT', 'Continuously Variable Transmission'), ('DCT', 'Dual Clutch Transmission'), ('AMT', 'Automated Manual Transmission'), ('DSG', 'Direct Shift Gearbox')], default='Manual', max_length=100, verbose_name='Transmission')),
                ('fuel_type', models.CharField(choices=[('Gasoline', 'Gasoline'), ('Ethanol', 'Ethanol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric'), ('CNG', 'Compressed Natural Gas'), ('LPG', 'Liquefied Petroleum Gas'), ('Biodiesel', 'Biodiesel')], default='Gasoline', max_length=50, verbose_name='Fuel Type')),
                ('num_doors', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of doors')),
                ('num_seats', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of seats')),
                ('year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Year')),
                ('mileage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Mileage (Km)')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price (R$)')),
            ],
            options={
                'verbose_name': 'Automobile',
                'verbose_name_plural': 'Automobiles',
                'db_table': 'automobile',
            },
        ),
        migrations.CreateModel(
            name='HistoricalAutomobile',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated at')),
                ('origin', models.CharField(choices=[('Manual', 'Manual'), ('Import', 'Import'), ('System', 'System'), ('Integration', 'Integration')], default='Manual', max_length=20, verbose_name='Origin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='Model')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='Color')),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='Brand')),
                ('engine', models.CharField(blank=True, max_length=100, null=True, verbose_name='Engine')),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic'), ('Semi-automatic', 'Semi-automatic'), ('CVT', 'Continuously Variable Transmission'), ('DCT', 'Dual Clutch Transmission'), ('AMT', 'Automated Manual Transmission'), ('DSG', 'Direct Shift Gearbox')], default='Manual', max_length=100, verbose_name='Transmission')),
                ('fuel_type', models.CharField(choices=[('Gasoline', 'Gasoline'), ('Ethanol', 'Ethanol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric'), ('CNG', 'Compressed Natural Gas'), ('LPG', 'Liquefied Petroleum Gas'), ('Biodiesel', 'Biodiesel')], default='Gasoline', max_length=50, verbose_name='Fuel Type')),
                ('num_doors', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of doors')),
                ('num_seats', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of seats')),
                ('year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Year')),
                ('mileage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Mileage (Km)')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price (R$)')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'historical Automobiles',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
