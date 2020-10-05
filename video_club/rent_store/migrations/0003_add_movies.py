# Generated by Django 3.0.5 on 2020-05-01 10:00
from django.db import migrations
import json
from pathlib import Path


def add_movies(apps, schema_editor):
    Movie = apps.get_model('rent_store', 'Movie')
    Category = apps.get_model('rent_store', 'Category')
    MovieCategoryAssociation = apps.get_model('rent_store', 'MovieCategoryAssociation')

    with open(Path('rent_store/data/movies.json'), 'r') as f:
        movies = json.load(f)

    for m in movies:
        m_dict = {"name": m["Title"],
                  "pub_date": m["Year"],
                  "duration": m["Duration"],
                  "rating": m["Rating"],
                  "description": m["Description"]
                  }
        movie = Movie(**m_dict)
        movie.save()

        for cat in m["Categories"]:
            category = Category.objects.get(uuid=cat)
            assoc = MovieCategoryAssociation(movie=movie, category=category)
            assoc.save()


class Migration(migrations.Migration):

    dependencies = [
        ('rent_store', '0002_add_categories'),
    ]

    operations = [
        migrations.RunPython(add_movies)
    ]
