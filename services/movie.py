from typing import Optional

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
    genres_ids: Optional[list[int]] = None,
    actors_ids: Optional[list[int]] = None
) -> QuerySet:
    movie_result = Movie.objects.all()
    if genres_ids:
        movie_result = movie_result.filter(genres__id__in=genres_ids)
    if actors_ids:
        movie_result = movie_result.filter(actors__id__in=actors_ids)

    return movie_result


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[list[int]] = None,
    actors_ids: Optional[list[int]] = None
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
