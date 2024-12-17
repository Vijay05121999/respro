# Generated by Django 3.2.8 on 2021-11-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=400)),
                ('Address_Type', models.CharField(choices=[('Work', 'Work'), ('Home', 'Home')], default='Work', max_length=20)),
                ('Phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Plan_Type', models.CharField(max_length=200)),
            ],
        ),
    ]