# Generated by Django 3.2.5 on 2021-08-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
            ],
        ),
    ]
