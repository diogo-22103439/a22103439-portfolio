# Generated by Django 4.0.4 on 2022-05-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_cadeira'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('descricao', models.TextField()),
            ],
        ),
    ]
