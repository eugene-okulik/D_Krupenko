import requests
import pytest

BASE_URL = "http://objapi.course.qa-practice.com/object"


@pytest.fixture()
def creating_and_deleting_fixture():
    post_req = requests.post(BASE_URL, json={'data': {'color': 'green', 'size': 'xxl'}, 'name': 'test_name'})
    yield post_req
    requests.delete(f"{BASE_URL}/{int(post_req.json()['id'])}")


@pytest.fixture()
def creating_fixture():
    post_req = requests.post(BASE_URL, json={'data': {'color': 'green', 'size': 'xxl'}, 'name': 'test_name'})
    return post_req


@pytest.fixture(scope="session")
def test_session_message():
    print("\nStart testing")
    yield
    print("Testing completed")


@pytest.fixture()
def func_message():
    print("\nbefore test")
    yield
    print("after test")


def test_get_request(func_message, test_session_message, creating_and_deleting_fixture):
    req = requests.get(f"{BASE_URL}/{int(creating_and_deleting_fixture.json()['id'])}")
    assert req.json()["id"] == creating_and_deleting_fixture.json()["id"]


@pytest.mark.parametrize("obj", [{'data': {'color': 'black', 'size': 's1'}, 'name': 'name1'},
                                 {'data': {'color': 'black2', 'size': 's2'}, 'name': 'name2'},
                                 {'data': {'color': 'black3', 'size': 's3'}, 'name': 'name3'}])
def test_post(func_message, obj):
    new_post = requests.post(BASE_URL,
                             json=obj)
    assert new_post.status_code == 200, "статус код не соответсвует ожидаемому"
    assert type(new_post.json()["name"]) == str, "невалидный формат данных поля name"
    assert type(new_post.json()["data"]) == dict, "невалидный формат данных поля data"
    assert type(new_post.json()["id"]) == int, "невалидный формат данных поля id"
    requests.delete(f"{BASE_URL}/{new_post.json()['id']}")


@pytest.mark.critical
def test_put(func_message, creating_and_deleting_fixture):
    obj = requests.put(
        f"{BASE_URL}/{int(creating_and_deleting_fixture.json()['id'])}",
        json={'data': {'color': 'black', 'size': 's', 'additional_field': 'lorem'},
              'name': 'test_name_2'},
    )
    assert obj.status_code == 200, "статус код не соответсвует ожидаемому"
    assert type(obj.json()["name"]) == str, "невалидный формат данных поля name"
    assert obj.json()["data"] == {'color': 'black', 'size': 's', 'additional_field': 'lorem'}, \
        "данные не обновлены"
    assert type(int(obj.json()['id'])) == int, "невалидный формат данных поля id"


@pytest.mark.medium
def test_patch(func_message, creating_and_deleting_fixture):
    obj = requests.patch(f"{BASE_URL}/{int(creating_and_deleting_fixture.json()['id'])}", json={'name': 'test888'})
    assert obj.status_code == 200, "статус код не соответсвует ожидаемому"
    assert obj.json()["name"] == "test888", "обновление не применено"


def test_delete(func_message, creating_fixture):
    delete_obj = requests.delete(f"{BASE_URL}/{int(creating_fixture.json()['id'])}")
    delete_obj_2 = requests.delete(f"{BASE_URL}/{int(creating_fixture.json()['id'])}")
    assert delete_obj.status_code == 200, "статус код не соответсвует ожидаемому"
    assert delete_obj_2.status_code == 404, "статус код не соответсвует ожидаемому"


@pytest.mark.skip("skip check")
def test_skip_test(func_message):
    print("skip check")
    pass
