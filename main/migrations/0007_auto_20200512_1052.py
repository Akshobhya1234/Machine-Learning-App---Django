# Generated by Django 2.0.12 on 2020-05-12 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200512_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchuser',
            old_name='password',
            new_name='FileName',
        ),
        migrations.RenameField(
            model_name='searchuser',
            old_name='phoneNumber',
            new_name='UploadCSV',
        ),
        migrations.RemoveField(
            model_name='searchuser',
            name='emailID',
        ),
        migrations.RemoveField(
            model_name='searchuser',
            name='userName',
        ),
    ]
