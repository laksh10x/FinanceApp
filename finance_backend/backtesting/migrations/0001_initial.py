# Generated by Django 4.2.16 on 2024-10-21 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_investment', models.FloatField()),
                ('buy_moving_average', models.IntegerField(default=50)),
                ('sell_moving_average', models.IntegerField(default=200)),
                ('symbol', models.CharField(default='AAPL', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BacktestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_return', models.FloatField()),
                ('max_drawdown', models.FloatField()),
                ('trades_executed', models.IntegerField()),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
                ('backtest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='backtesting.backtest')),
            ],
        ),
    ]