# Generated by Django 2.1.5 on 2019-02-10 21:21

from django.db import migrations, models
import django.db.models.deletion
import recite.fields
import recite.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quran', '0002_load_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segments', recite.fields.SegmentsField()),
                ('audio', models.FileField(upload_to=recite.models.Recitation.get_audio_directory)),
                ('ayah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recitations', to='quran.Ayah')),
            ],
        ),
        migrations.CreateModel(
            name='Reciter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bitrate', models.PositiveIntegerField(blank=True, help_text='Bitrate of an audio file', null=True)),
                ('style', models.CharField(blank=True, help_text="Qur'an reading style", max_length=20)),
                ('slug', models.SlugField(help_text='Short unique label for name, containing only letters and hyphens. ', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='recitation',
            name='reciter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recitations', to='recite.Reciter'),
        ),
    ]
