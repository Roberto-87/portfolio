# Generated by Django 4.1.1 on 2022-10-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPortfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_onmouseover',
            field=models.ImageField(default='portfolio/images/', upload_to='portfolio/images/'),
        ),
    ]
