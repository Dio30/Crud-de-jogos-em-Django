# Generated by Django 4.0.5 on 2022-06-01 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_jogo', models.CharField(max_length=30)),
                ('tipo_de_jogo', models.CharField(max_length=30)),
                ('valor_do_jogo', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('descrição_do_jogo', models.TextField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Jogo',
                'verbose_name_plural': 'Jogos',
                'ordering': ['nome_do_jogo'],
            },
        ),
    ]