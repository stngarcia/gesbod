# Generated by Django 2.1.7 on 2019-03-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_auto_20190324_0434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, max_length=250, null=True, verbose_name='Reseña')),
                ('habilitado', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('nombre',)},
        ),
        migrations.AlterModelOptions(
            name='editorial',
            options={'ordering': ('nombre',)},
        ),
        migrations.AddField(
            model_name='categoria',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='editorial',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]