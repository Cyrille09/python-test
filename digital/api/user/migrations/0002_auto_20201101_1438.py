# Generated by Django 3.0.8 on 2020-11-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='session_token',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
