# Generated by Django 5.0.1 on 2024-06-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
