# Generated by Django 2.0 on 2020-06-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=800)),
            ],
        ),
    ]
