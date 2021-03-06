# Generated by Django 3.0.5 on 2020-04-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', null=True, to='catalog.Genre'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
