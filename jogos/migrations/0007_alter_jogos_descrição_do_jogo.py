# Generated by Django 4.0.5 on 2022-06-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0006_alter_jogos_descrição_do_jogo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogos',
            name='descrição_do_jogo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
