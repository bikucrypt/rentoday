# Generated by Django 3.1.8 on 2021-04-19 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20210419_0932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='my_order',
        ),
    ]