# Generated by Django 3.0.3 on 2020-02-28 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.BooleanField()),
                ('kills', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RelationsGroupHeroPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('networth', models.IntegerField()),
                ('kda', models.FloatField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Team')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Hero')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numMembers', models.SmallIntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.BooleanField()),
                ('date', models.DateField()),
                ('dire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dire', to='games.Team')),
                ('radiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='radiant', to='games.Team')),
            ],
        ),
    ]
