# Generated by Django 2.0.13 on 2019-04-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20190430_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default=1, upload_to='image'),
            preserve_default=False,
        ),
    ]
