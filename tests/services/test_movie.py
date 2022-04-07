import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture
def movie_dao():
    dao = MovieDAO(None)
    dao.get_one = MagicMock('houston we have a problem')
    dao.get_all =  MagicMock('houston we have a problem')
    dao.update = MagicMock('houston we have a problem')
    dao.delete = MagicMock('houston we have a problem')
    dao.create = MagicMock('houston we have a problem')
    return dao


@pytest.fixture
def movie_service(movie_dao):
    return MovieService(dao=movie_dao)


def test_get_one(movie_service):
    movie_service.dao.get_one.return_value = {
            'id': 1,
            'title': 'test',
            'description': 'text',
            'trailer': 'network',
            'year': '1978',
            'rating': '6',
            'genre_id': '2',
            'director_id': '3',
        }
    assert movie_service.get_one(1) == {
            'id': 1,
            'title': 'test',
            'description': 'text',
            'trailer': 'network',
            'year': '1978',
            'rating': '6',
            'genre_id': '2',
            'director_id': '3',
        }


def test_get_all(movie_service):
    movie_service.dao.get_all.return_value = [
        {
            'id': 1,
            'title': 'test',
            'description': 'text',
            'trailer': 'network',
            'year': '1978',
            'rating': '6',
            'genre_id': '2',
            'director_id': '3',
        },
        {
            'id': 2,
            'title': 'test_1',
            'description': 'text_1',
            'trailer': 'network_2',
            'year': '1979',
            'rating': '7',
            'genre_id': '8',
            'director_id': '4',
        }
    ]

    assert movie_service.get_all() == [
        {
            'id': 1,
            'title': 'test',
            'description': 'text',
            'trailer': 'network',
            'year': '1978',
            'rating': '6',
            'genre_id': '2',
            'director_id': '3',
        },
        {
            'id': 2,
            'title': 'test_1',
            'description': 'text_1',
            'trailer': 'network_2',
            'year': '1979',
            'rating': '7',
            'genre_id': '8',
            'director_id': '4',
        }
    ]



def test_create(movie_service):
    movie_service.dao.create.return_value = {
        'id': 1,
        'title': 'test',
        'description': 'text',
        'trailer': 'network',
        'year': '1978',
        'rating': '6',
        'genre_id': '2',
        'director_id': '3',
    }


    assert movie_service.create != None



def test_delete(movie_service):
    movie_service.delete(1)
    movie_service.dao.delete.assert_called_once_with(1)

def test_update(movie_service):
    movie_service.update({})
    movie_service.dao.update.assert_called_once_with({})