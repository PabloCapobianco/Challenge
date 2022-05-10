# Generated by Django 2.2.16 on 2022-05-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('DNI', models.EmailField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Materias_en_curso', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alumno', models.PositiveIntegerField()),
                ('Apellido', models.CharField(max_length=100)),
                ('Materia', models.CharField(max_length=100)),
                ('Fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnicatura_en_Programación',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Materia', models.CharField(max_length=100)),
                ('Alumnos_inscriptos', models.CharField(default='Ninguno', max_length=100)),
                ('Horas_semanales', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
