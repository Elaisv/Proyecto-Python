# Generated by Django 4.0.4 on 2022-06-02 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios_Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('detalle', models.CharField(max_length=100)),
            ],
        ),
    ]
