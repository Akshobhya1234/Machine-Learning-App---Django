# Generated by Django 2.0.12 on 2020-05-19 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_searchuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchuser',
            name='UserName',
            field=models.CharField(default='abc', max_length=200),
            preserve_default=False,
        ),
    ]