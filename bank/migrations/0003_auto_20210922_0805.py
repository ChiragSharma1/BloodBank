# Generated by Django 3.2.5 on 2021-09-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20210922_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='', max_length=5, null=True),
        ),
    ]