# Generated by Django 4.0.4 on 2022-07-02 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion_junkie_app', '0004_remove_movie_favorites_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_url',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]