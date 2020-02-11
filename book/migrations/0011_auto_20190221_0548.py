# Generated by Django 2.0.7 on 2019-02-21 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20190130_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]