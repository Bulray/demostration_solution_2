import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture
def director_dao():
    dao = DirectorDAO(None)
    dao.get_one = MagicMock('houston we have a problem')
    dao.get_all =  MagicMock('houston we have a problem')
    dao.update =  MagicMock('houston we have a problem')
    dao.delete =  MagicMock('houston we have a problem')
    dao.create =  MagicMock('houston we have a problem')
    return dao


@pytest.fixture
def director_service(director_dao):
    return DirectorService(dao=director_dao)


@pytest.mark.parametrize(
    'data',
    (
            {
                'id': 1,
                'name': 'test',
            },
            {
                'id': 2,
                'name': 'test_name',
            }
    )
)
def test_get_one(director_service, data):
    director_service.dao.get_one.return_value = data
    assert director_service.get_one(1) == data


@pytest.mark.parametrize(
    'length, data',
    (
            (
                    2,
                    [
                        {
                            'id': 1,
                            'name': 'test',
                        },
                        {
                            'id': 2,
                            'name': 'test_name',
                        },
                    ],
            ),
            (
                    0,
                    [],
            )
    ),
)
def test_get_all(director_service, length, data):
    director_service.dao.get_all.return_value == data
    result = director_service.get_all()
    assert isinstance(result, list)
    assert len(result) == length
    assert result == data


def test_create(director_service):
    director_service.dao.create.return_value = {
        'id': 1,
        'name': 'test'
    }
    assert director_service.create != None

@pytest.mark.parametrize(
    'original_data, modified_data',
    (
            (
            {
                'id': 1,
                'name': 'test',
            },
            {
                'id': 1,
                'name': 'changed_name',
            },
            ),
    ),
)

def test_partially_update(director_service, original_data, modified_data):
    director_service.dao.get_one.return_value = original_data
    director_service.partially_update(modified_data)
    director_service.dao.get_one.assert_called_once_with(original_data['id'])

    director_service.dao.update.assert_called_once_with(modified_data)


@pytest.mark.parametrize(
    'original_data, modified_data',
    (
            (
            {
                'id': 1,
                'name': 'test',
            },
            {
                'id': 1,
                'ter': 'ytr',
            },
            ),
    ),
)
def test_partially_update_with_wrong_fields(director_service, original_data, modified_data):
    director_service.get_one.return_value = original_data
    director_service.partially_update(modified_data)
    director_service.dao.update.assert_called_once_with(original_data)


def test_delete(director_service):
    director_service.delete(1)
    director_service.dao.delete.assert_called_once_with(1)

def test_update(director_service):
    director_service.update({})
    director_service.dao.update.assert_called_once_with({})






