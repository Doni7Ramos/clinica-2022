# Generated by Django 4.1.1 on 2022-09-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_medico_especialidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('descricao', models.CharField(max_length=1000)),
            ],
        ),
    ]
