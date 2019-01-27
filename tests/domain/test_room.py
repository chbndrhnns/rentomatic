import uuid
import pytest
from rentomatic.domain import room as r


@pytest.fixture
def code():
    return uuid.uuid4()


@pytest.fixture
def room_dict(code):
    return {
        'code': code,
        'size': 200,
        'price': 10,
        'longitude': -0.9998975,
        'latitude': 51.75436293
    }


def test__room_model__init():
    code = uuid.uuid4()
    room = r.Room(
        code, size=200, price=10, longitude=-0.9998975, latitude=51.75436293)

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.9998975
    assert room.latitude == 51.75436293


def test__room_model__from_dict(room_dict, code):
    room = r.Room.from_dict(room_dict)

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.9998975
    assert room.latitude == 51.75436293


def test__room_model__to_dict(room_dict):
    room = r.Room.from_dict(room_dict)

    assert room.to_dict() == room_dict


def test__room_model__comparison(room_dict):
    room1 = r.Room.from_dict(room_dict)
    room2 = r.Room.from_dict(room_dict)

    assert room1 == room2
