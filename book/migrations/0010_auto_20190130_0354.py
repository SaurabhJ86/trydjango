# Generated by Django 2.0.7 on 2019-01-30 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('about', models.TextField()),
                ('genre', models.ManyToManyField(blank=True, related_name='author_genre', to='book.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author_new',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.Author'),
        ),
    ]