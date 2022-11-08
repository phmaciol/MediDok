# Generated by Django 3.1.4 on 2022-03-23 09:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0001_initial'),
        ('Placowki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term_day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_date', models.DateField(null=True, verbose_name='Data')),
                ('work_time', models.TimeField(verbose_name='Godzina wizyty')),
                ('work_day', models.CharField(choices=[('0', 'Poniedziałek'), ('1', 'Wtorek'), ('2', 'Środa'), ('3', 'Czwartek'), ('4', 'Piątek'), ('5', 'Sobota'), ('6', 'Niedziela')], max_length=100, null=True, verbose_name='Dzień tygodnia')),
                ('work_type', models.CharField(max_length=100, null=True, verbose_name='Typ terminarza')),
                ('work_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Profile.personal_med', verbose_name='Osoba personelu')),
                ('work_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Placowki.unit', verbose_name='Jednostka')),
            ],
            options={
                'verbose_name_plural': 'Terminarz',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(choices=[('0', 'Lekarz'), ('1', 'Pielęgniarka'), ('2', 'Położna')], max_length=100, null=True, verbose_name='Typ terminarza')),
                ('work_start', models.TimeField(verbose_name='Początek wizyty')),
                ('work_stop', models.TimeField(verbose_name='Koniec wizyty')),
                ('work_day', models.IntegerField(choices=[(0, 'Poniedziałek'), (1, 'Wtorek'), (2, 'Środa'), (3, 'Czwartek'), (4, 'Piątek'), (5, 'Sobota'), (6, 'Niedziela')], null=True, verbose_name='Dzień tygodnia')),
                ('work_time', models.IntegerField(null=True, verbose_name='Czas trwania wizyty')),
                ('work_start_date', models.DateField(null=True, verbose_name='Data początku')),
                ('work_stop_date', models.DateField(null=True, verbose_name='Data początku')),
                ('work_date', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Data początku')),
                ('work_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Profile.personal_med', verbose_name='Osoba personelu')),
                ('work_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Placowki.unit', verbose_name='Jednostka')),
            ],
            options={
                'verbose_name_plural': 'Harmonogram',
            },
        ),
    ]