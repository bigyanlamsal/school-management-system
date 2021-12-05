# Generated by Django 3.2.5 on 2021-12-05 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_notice_info_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('level', models.TextField(max_length=1000)),
                ('image_vacancy', models.ImageField(blank=True, upload_to='media/students/vacancy_file/')),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='notice_info',
            name='passport',
            field=models.ImageField(blank=True, upload_to='media/students/notices_file/'),
        ),
    ]