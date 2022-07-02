# Generated by Django 4.0.4 on 2022-07-02 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion_junkie_app', '0005_movie_poster_url'),
        ('users_app', '0003_alter_user_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='users', to='opinion_junkie_app.movie'),
        ),
    ]
