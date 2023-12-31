# Generated by Django 4.1.1 on 2023-01-27 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Van',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(blank=True, max_length=12, null=True)),
                ('vcost', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=12, null=True)),
                ('city', models.CharField(blank=True, max_length=12, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('van', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modelapp.van')),
            ],
        ),
    ]
