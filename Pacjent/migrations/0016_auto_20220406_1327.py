# Generated by Django 3.1.4 on 2022-04-06 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Placowki', '0004_auto_20220401_1909'),
        ('Pacjent', '0015_auto_20220405_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dekl',
            name='idunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Placowki.unit', verbose_name='Jednostka'),
        ),
    ]
