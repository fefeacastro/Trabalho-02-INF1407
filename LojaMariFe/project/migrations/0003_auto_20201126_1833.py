# Generated by Django 3.1.3 on 2020-11-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20201126_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(help_text='Imagem do produto', upload_to='project/static/images/'),
        ),
    ]
