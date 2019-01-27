import pytest

from rentomatic.domain import room as r
from rentomatic.repository import memrepo


@pytest.fixture
def room_dicts():
    return [{
        'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
        'size': 215,
        'price': 39,
        'longitude': -0.09998975,
        'latitude': 51.75436293,
    },
            {
                'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
                'size': 405,
                'price': 66,
                'longitude': 0.18228006,
                'latitude': 51.74640997,
            },
            {
                'code': '913694c6-435a-4366-ba0d-da5334a611b2',
                'size': 56,
                'price': 60,
                'longitude': 0.27891577,
                'latitude': 51.45994069,
            },
            {
                'code': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',
                'size': 93,
                'price': 48,
                'longitude': 0.33894476,
                'latitude': 51.39916678,
            }]


def test__repository_list__without_parameters(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    rooms = [r.Room.from_dict(i) for i in room_dicts]

    assert repo.list() == rooms

def test__repository_list__with_equal_prices(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    repo_rooms = repo.list(
        filters={'price__eq': 60}
    )

    assert len(repo_rooms) == 1
    assert repo_rooms[0].code == '913694c6-435a-4366-ba0d-da5334a611b2'

def test__repository_list__with_prices_less_than_filter(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    repo_rooms = repo.list(filters={
        'price__lt': 60
    })

    assert len(repo_rooms) == 2
    assert set([r.code for r in repo_rooms]) == {
        'eed76e77-55c1-41ce-985d-ca49bf6c0585',
        'f853578c-fc0f-4e65-81b8-566c5dffa35a'
    }

def test__repository_list__with_price_greater_than_filter(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    repo_rooms = repo.list(
        filters={'price__gt':48}
    )

    assert len(repo_rooms) == 2
    assert set([r.code for r in repo_rooms]) == {
        'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
        '913694c6-435a-4366-ba0d-da5334a611b2'
    }

def test__repository_list__with_price_between_filters(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    repo_rooms = repo.list(filters={
        'price__lt': 66,
        'price__gt': 48
    })

    assert len(repo_rooms) ==1
    assert repo_rooms[0].code == '913694c6-435a-4366-ba0d-da5334a611b2'