# Generated by Django 3.0.3 on 2020-02-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fia', '0004_auto_20200218_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='subject',
            field=models.CharField(default='주제', max_length=50),
        ),
    ]
