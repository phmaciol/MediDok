# Generated by Django 3.1.4 on 2022-03-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pacjent', '0008_visit_id10'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='status',
            field=models.CharField(choices=[('0', 'Zarejestrowana'), ('1', 'Zapalnowana'), ('2', 'Do realizacji'), ('3', 'Zrealizowana')], max_length=100, null=True, verbose_name='Status aktualny'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='type_visit',
            field=models.CharField(choices=[('0', 'Receptowa'), ('1', 'Porada'), ('2', 'Teleporada'), ('3', 'Z skierowaniem'), ('4', 'Kontynuacja'), ('5', '')], default='5', max_length=100, verbose_name='Rodzajy Wizyty'),
        ),
    ]
