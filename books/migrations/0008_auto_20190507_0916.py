# Generated by Django 2.2 on 2019-05-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20190505_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='co_author_name',
        ),
        migrations.AddField(
            model_name='book',
            name='co_author_name',
            field=models.ManyToManyField(related_name='co_author', to='books.Author'),
        ),
    ]
