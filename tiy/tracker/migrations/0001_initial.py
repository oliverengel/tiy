# Generated by Django 3.1.7 on 2021-03-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('asset_buy', models.CharField(max_length=3)),
                ('asset_buy_quantity', models.DecimalField(decimal_places=8, max_digits=12)),
                ('asset_sell', models.CharField(max_length=3)),
                ('asset_sell_quantity', models.DecimalField(decimal_places=8, max_digits=12)),
                ('fee_in_asset', models.CharField(max_length=3)),
                ('fee_quantity', models.DecimalField(decimal_places=8, max_digits=12)),
                ('broker', models.CharField(max_length=20)),
                ('note', models.TextField(blank=True)),
            ],
        ),
    ]
