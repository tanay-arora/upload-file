# Generated by Django 4.0.6 on 2022-07-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_users_attende_alter_users_startup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='ticketid',
            field=models.CharField(default='', editable=None, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(default='', editable=None, max_length=120),
        ),
    ]
