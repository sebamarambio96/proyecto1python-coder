# Generated by Django 4.2.1 on 2023-05-28 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('control_estudios', '0006_remove_curso_creador_delete_entregable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='fecha_publicacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
