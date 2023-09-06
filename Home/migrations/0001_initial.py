# Generated by Django 3.2 on 2021-11-24 19:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageModel',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('release_date', models.CharField(default='None', max_length=70)),
                ('short_intro', models.TextField(max_length=700)),
                ('IMDb_RATING', models.CharField(default=None, max_length=50)),
                ('poster', models.ImageField(upload_to='Posters/')),
                ('summary', models.TextField(max_length=1600)),
                ('trailer', models.CharField(blank=True, max_length=650, null=True)),
                ('download_link_1080', models.CharField(blank=True, max_length=650, null=True)),
                ('download_link_720', models.CharField(blank=True, max_length=650, null=True)),
                ('download_link_480', models.CharField(blank=True, max_length=650, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('director', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.director')),
                ('genre', models.ManyToManyField(to='Home.Genre')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
