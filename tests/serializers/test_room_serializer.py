import json
import uuid
import pytest

from rentomatic.serializers import room_json_serializer as ser
from rentomatic.domain import room as r


@pytest.fixture
def code():
    return uuid.uuid4()


def test__serialize_domain__room(code):
    room = r.Room(
        code, size=200, price=10, longitude=-0.9998975, latitude=51.75436293)

    expected_json = """
    {{
        "code": "{}",
        "size": 200,
        "price": 10,
        "longitude": -0.9998975,
        "latitude": 51.75436293
    }}
    """.format(code)

    json_room = json.dumps(room, cls=ser.RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
