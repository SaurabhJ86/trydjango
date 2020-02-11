# Generated by Django 2.0.7 on 2019-02-21 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20190221_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_new',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='under_author', to='book.Author'),
        ),
    ]