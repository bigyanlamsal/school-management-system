# Generated by Django 3.2.5 on 2021-12-01 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0006_remove_notices_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
