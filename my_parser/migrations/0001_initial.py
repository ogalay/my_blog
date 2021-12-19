# Generated by Django 3.1.4 on 2020-12-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title ')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Sub_title ')),
                ('url', models.CharField(max_length=200, verbose_name='Url ')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
