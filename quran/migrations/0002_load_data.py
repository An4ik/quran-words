# Generated by Django 2.1 on 2018-09-08 09:13

from os import path
from django.db import migrations
from django.core.management import call_command

fixture_surahs = 'surah_list.json'
fixture_ayahs = 'ayah_list.json'


class LoadData:
    """Class for loading data into DataBase from fixture files"""
    def __init__(self, fixture_data):
        self.fixture_dir = path.abspath(
            path.join(path.dirname(__file__), '../fixtures/'))
        self.fixture_data = fixture_data

    def __call__(self, apps, schema_editor):
        fixture_file = path.join(self.fixture_dir, self.fixture_data)
        call_command('loaddata', fixture_file)


class UnloadData:
    """Class for deleting all entries from a given (app, model) pair."""
    def __init__(self, app, model):
        self.app = app
        self.model = model

    def __call__(self, apps, schema_editor):
        Model = apps.get_model(self.app, self.model)
        Model.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quran', '0001_initial'),
    ]

    operations = [
        # Loading surahs
        migrations.RunPython(
            LoadData(fixture_surahs),
            reverse_code=UnloadData('quran', 'Surah')),
        # Loading ayahs
        migrations.RunPython(
            LoadData(fixture_ayahs),
            reverse_code=UnloadData('quran', 'Ayah')),
    ]
