# Generated by Django 4.2.6 on 2024-02-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_category_policy_question_policyrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='questiondata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
