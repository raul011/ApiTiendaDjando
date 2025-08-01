# Generated by Django 5.2 on 2025-04-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
