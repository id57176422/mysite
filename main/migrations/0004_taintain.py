# Generated by Django 3.1.3 on 2023-02-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230209_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='taintain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('maintain', models.CharField(max_length=100)),
            ],
        ),
    ]
