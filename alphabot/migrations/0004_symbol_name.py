# Generated by Django 4.0.6 on 2022-07-22 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alphabot', '0003_rename_outstandingshares_symbol_outstanding_shares_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='symbol',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]