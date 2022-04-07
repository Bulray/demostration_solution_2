import pytest
from unittest.mock import MagicMock

from dao.genre import GenreDAO
from service.genre import GenreService


@pytest.fixture
def genre_dao():
    dao = GenreDAO(None)
    dao.get_one = MagicMock('houston we have a problem')
    dao.get_all = MagicMock('houston we have a problem')
    dao.update = MagicMock('houston we have a problem')
    dao.delete = MagicMock('houston we have a problem')
    dao.create = MagicMock('houston we have a problem')
    return dao


@pytest.fixture
def genre_service(genre_dao):
    return GenreService(dao=genre_dao)


def test_get_one(genre_service):
    genre_service.dao.get_one.return_value = {
        'id': '1',
        'name': 'test'
    }
    assert genre_service.get_one(1) == {
        'id': '1',
        'name': 'test',
    }


def test_get_all(genre_service):
    genre_service.dao.get_all.return_value = [
        {
            'id': 1,
            'name': 'test'
        },
        {
            'id': 2,
            'name': 'test_name'
        }
    ]

    assert genre_service.get_all() == [
        {
            'id': 1,
            'name': 'test'
        },
        {
            'id': 2,
            'name': 'test_name'
        },
    ]


def test_create(genre_service):
    genre_service.dao.create.return_value = {
        'id': 1,
        'name': 'test'
    }

    assert genre_service.create != None


def test_delete(genre_service):
    genre_service.delete(1)
    genre_service.dao.delete.assert_called_once_with(1)

def test_update(genre_service):
    genre_service.update({})
    genre_service.dao.update.assert_called_once_with({})