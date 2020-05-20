# Generated by Django 3.0.6 on 2020-05-18 20:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'Actors and directors', 'verbose_name_plural': 'Actors and directors'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Genre', 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Film', 'verbose_name_plural': 'Films'},
        ),
        migrations.AlterModelOptions(
            name='movieshots',
            options={'verbose_name': 'Film shot', 'verbose_name_plural': 'Film shots'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Rating', 'verbose_name_plural': 'Rating'},
        ),
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Rating Star', 'verbose_name_plural': 'Rating Stars'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
        migrations.AddField(
            model_name='movie',
            name='running_time',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Running time'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='age',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(upload_to='artists/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='film_actor', to='moviesapp.Artist', verbose_name='Actors'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.PositiveIntegerField(default=0, help_text='USD', verbose_name='Budget'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moviesapp.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(max_length=50, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='film_director', to='moviesapp.Artist', verbose_name='Director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Draft'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='fees_in_usa',
            field=models.PositiveIntegerField(default=0, help_text='USD', verbose_name='Fees in USA'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='fees_in_world',
            field=models.PositiveIntegerField(default=0, help_text='USD', verbose_name='Fees in world'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='moviesapp.Genre', verbose_name='Genres'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='movies/', verbose_name='Poster'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tagline',
            field=models.CharField(default='', max_length=100, verbose_name='Tagline'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='world_premiere',
            field=models.DateField(default=datetime.date.today, verbose_name='World premiere'),
        ),
        migrations.AlterField(
            model_name='movieshots',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='movieshots',
            name='image',
            field=models.ImageField(upload_to='movie_shots/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='movieshots',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesapp.Movie', verbose_name='Movie'),
        ),
        migrations.AlterField(
            model_name='movieshots',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='ip',
            field=models.CharField(max_length=32, verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='moviesapp.Movie', verbose_name='Movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesapp.RatingStar', verbose_name='Star'),
        ),
        migrations.AlterField(
            model_name='ratingstar',
            name='value',
            field=models.SmallIntegerField(default=0, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesapp.Movie', verbose_name='Movie'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='moviesapp.Reviews', verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text',
            field=models.TextField(max_length=4296, verbose_name='Message'),
        ),
    ]