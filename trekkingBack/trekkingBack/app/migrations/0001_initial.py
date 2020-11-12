# Generated by Django 2.2 on 2020-11-11 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol_Users',
            fields=[
                ('Id_rol', models.IntegerField(primary_key=True, serialize=False)),
                ('Name_rol', models.CharField(max_length=100)),
                ('Description_rol', models.CharField(max_length=100)),
                ('Activo_rol', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id_user', models.IntegerField(primary_key=True, serialize=False)),
                ('FirtName_user', models.CharField(max_length=100)),
                ('LastName_user', models.CharField(max_length=100)),
                ('User_login', models.CharField(max_length=100)),
                ('Pass_login', models.CharField(max_length=100)),
                ('Activo_user', models.BooleanField()),
                ('Id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Rol_Users')),
            ],
        ),
    ]
