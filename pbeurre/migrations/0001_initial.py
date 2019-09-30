# Generated by Django 3.0a1 on 2019-09-29 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('picture', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('avatar', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('category_tags1', models.CharField(max_length=250)),
                ('category_tags2', models.CharField(max_length=600)),
                ('nutri_score', models.CharField(max_length=3)),
                ('repere_fat100g', models.CharField(max_length=3)),
                ('repere_saturatedfat100g', models.CharField(max_length=3)),
                ('repere_sugars100g', models.CharField(max_length=3)),
                ('repere_saltunit', models.CharField(max_length=3)),
                ('picture', models.URLField(null=True)),
                ('url', models.CharField(max_length=150)),
                ('stores', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.URLField(null=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pbeurre.Food')),
            ],
        ),
    ]
