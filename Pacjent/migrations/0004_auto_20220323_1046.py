# Generated by Django 3.1.4 on 2022-03-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pacjent', '0003_auto_20220323_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='description',
            field=models.TextField(null=True, verbose_name='Opis'),
        ),
    ]