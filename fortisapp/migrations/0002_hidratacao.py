# Generated by Django 5.1.1 on 2024-09-28 01:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortisapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hidratacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_agua', models.PositiveIntegerField()),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
