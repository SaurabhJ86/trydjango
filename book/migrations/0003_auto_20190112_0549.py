# Generated by Django 2.0.7 on 2019-01-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20190112_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ratings',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
