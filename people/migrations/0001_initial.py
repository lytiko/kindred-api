# Generated by Django 2.2.8 on 2020-03-03 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(blank=True, max_length=256)),
                ('description', models.TextField(blank=True)),
                ('started', models.DateField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'people',
                'db_table': 'people',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('people', models.ManyToManyField(blank=True, related_name='tags', to='people.Person')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('person1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_relationships1', to='people.Person')),
                ('person2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_relationships2', to='people.Person')),
            ],
            options={
                'db_table': 'relationships',
            },
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('level', models.IntegerField(choices=[(1, 'Text'), (2, 'Voice'), (3, 'In Person')])),
                ('description', models.TextField(blank=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='people.Person')),
            ],
            options={
                'db_table': 'interactions',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Handle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handles', to='people.Person')),
            ],
            options={
                'db_table': 'handles',
                'ordering': ['name'],
            },
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='unique name'),
        ),
    ]
