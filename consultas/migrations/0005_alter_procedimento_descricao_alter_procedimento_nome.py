# Generated by Django 4.1.1 on 2022-09-24 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0004_alter_procedimento_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedimento',
            name='descricao',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
