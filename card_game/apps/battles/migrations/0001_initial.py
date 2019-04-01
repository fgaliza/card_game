import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BattleRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoundResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round_results', to='cards.Card')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round_results', to='players.Player')),
            ],
        ),
        migrations.AddField(
            model_name='battleround',
            name='round_results',
            field=models.ManyToManyField(related_name='battle_round', to='battles.RoundResult'),
        ),
        migrations.AddField(
            model_name='battle',
            name='battle_rounds',
            field=models.ManyToManyField(related_name='battles', to='battles.BattleRound'),
        ),
        migrations.AddField(
            model_name='battle',
            name='players',
            field=models.ManyToManyField(related_name='battles', to='players.Player'),
        ),
    ]
