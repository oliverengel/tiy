# Generated by Django 3.1.7 on 2021-03-27 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_assetaccount_trade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetaccount',
            name='trade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assetAccount_trade', to='tracker.trade'),
        ),
    ]
