# Generated by Django 2.2.2 on 2023-05-22 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Square',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('rotation', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Trunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('square', models.ManyToManyField(to='tree.Square')),
            ],
        ),
        migrations.CreateModel(
            name='Triangle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.ManyToManyField(to='tree.Coordinate')),
            ],
        ),
        migrations.AddField(
            model_name='square',
            name='triangles',
            field=models.ManyToManyField(to='tree.Triangle'),
        ),
    ]
