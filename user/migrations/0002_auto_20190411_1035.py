# Generated by Django 2.2 on 2019-04-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='platform',
            field=models.CharField(choices=[('android', 'android'), ('ios', 'ios')], default='android', max_length=10),
        ),
    ]
