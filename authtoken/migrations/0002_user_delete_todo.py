# Generated by Django 5.0 on 2023-12-17 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
