# Generated by Django 5.2.1 on 2025-05-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('file', models.FileField(blank=True, null=True, upload_to='books/')),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
