# Generated by Django 4.0.6 on 2022-07-13 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_ticket_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='cost',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='not_available',
            field=models.ManyToManyField(blank=True, related_name='not_available', to='event.feature'),
        ),
    ]
