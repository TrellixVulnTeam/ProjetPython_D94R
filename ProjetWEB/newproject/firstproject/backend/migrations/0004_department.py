# Generated by Django 2.2 on 2019-05-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_docteur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='post_image')),
            ],
        ),
    ]