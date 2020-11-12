# Generated by Django 2.2 on 2020-11-12 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_treeking',
            fields=[
                ('Id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('Name_tipo', models.CharField(max_length=100)),
                ('Description_tipo', models.CharField(max_length=5000)),
                ('Active_tipo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Treeking',
            fields=[
                ('Id_treeking', models.AutoField(primary_key=True, serialize=False)),
                ('Name_treeking', models.CharField(max_length=100)),
                ('Description_treekingr', models.CharField(max_length=5000)),
                ('ImageBase', models.ImageField(max_length=255, upload_to='images/')),
                ('Activo_treeking', models.BooleanField()),
                ('Tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tipos', to='app.Tipo_treeking')),
            ],
        ),
    ]
