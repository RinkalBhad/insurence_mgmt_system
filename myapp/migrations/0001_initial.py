# Generated by Django 4.2.6 on 2024-02-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usesignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=13)),
                ('number', models.BigIntegerField()),
                ('address', models.TextField()),
                ('pic', models.ImageField(upload_to='media')),
            ],
        ),
    ]
