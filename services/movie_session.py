from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie=Movie.objects.get(id=movie_id),
                                cinema_hall=CinemaHall.objects.get
                                (id=cinema_hall_id))


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    film = MovieSession.objects.get(id=session_id)

    if show_time:
        film.show_time = show_time

    if movie_id:
        film.movie_id = movie_id

    if cinema_hall_id:
        film.cinema_hall_id = cinema_hall_id
    film.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()