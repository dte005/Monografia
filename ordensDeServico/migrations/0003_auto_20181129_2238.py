# Generated by Django 2.1.3 on 2018-11-30 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordensDeServico', '0002_auto_20181129_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordensservico',
            name='os_numero',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]