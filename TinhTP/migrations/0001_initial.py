# Generated by Django 3.0.4 on 2020-03-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TinhTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaTinh', models.IntegerField(default=0)),
                ('TenTinh', models.CharField(max_length=50)),
            ],
        ),
    ]