# Generated by Django 2.1.3 on 2018-12-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascensor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='ciudad',
        ),
        migrations.AddField(
            model_name='cliente',
            name='region',
            field=models.CharField(default='region', max_length=50),
            preserve_default=False,
        ),
    ]