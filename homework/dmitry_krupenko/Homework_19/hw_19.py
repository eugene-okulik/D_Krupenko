import requests

BASE_URL = "http://objapi.course.qa-practice.com/object"


def print_response(response, label):
    print(f"\n--- {label} ---")
    print("Status code:", response.status_code)
    try:
        print("JSON:", response.json())
    except ValueError:
        print("Text:", response.text)


def get_id(response):
    try:
        return int(response.json()["id"])
    except (KeyError, ValueError, TypeError):
        raise AssertionError("id отсутствует или не приводится к int")


def post_object():
    response = requests.post(
        BASE_URL,
        json={
            'data': {'color': 'green', 'size': 'xxl'},
            'name': 'test_name'
        }
    )
    print_response(response, "POST object")
    return response


def put_object(obj_id):
    response = requests.put(
        f"{BASE_URL}/{int(obj_id)}",
        json={
            'data': {'color': 'black', 'size': 's', 'additional_field': 'lorem'},
            'name': 'test_name_2'
        }
    )
    print_response(response, f"PUT object {obj_id}")
    return response


def patch_object(obj_id):
    response = requests.patch(
        f"{BASE_URL}/{int(obj_id)}",
        json={'name': 'no_name'}
    )
    print_response(response, f"PATCH object {obj_id}")
    return response


def delete_object(obj_id):
    response = requests.delete(f"{BASE_URL}/{int(obj_id)}")
    print_response(response, f"DELETE object {obj_id}")
    return response


def post_test():
    obj = post_object()
    obj_id = get_id(obj)

    try:
        assert obj.status_code == 200, "статус код не соответсвует ожидаемому"
        assert isinstance(obj.json()["name"], str), "невалидный формат данных поля name"
        assert isinstance(obj.json()["data"], dict), "невалидный формат данных поля data"
        assert isinstance(obj_id, int), "невалидный формат данных поля id"
    except AssertionError as a:
        print("POST request error:", a)

    delete_object(obj_id)


def put_test():
    obj = post_object()
    obj_id = get_id(obj)

    put_obj = put_object(obj_id)
    put_id = get_id(put_obj)

    try:
        assert put_obj.status_code == 200, "статус код не соответсвует ожидаемому"
        assert isinstance(put_obj.json()["name"], str), "невалидный формат данных поля name"
        assert put_obj.json()["data"] == {
            'color': 'black',
            'size': 's',
            'additional_field': 'lorem'
        }, "данные не обновлены"
        assert isinstance(put_id, int), "невалидный формат данных поля id"
    except AssertionError as a:
        print("PUT request error:", a)

    delete_object(put_id)


def patch_test():
    obj = post_object()
    obj_id = get_id(obj)

    patch_obj = patch_object(obj_id)
    patch_id = get_id(patch_obj)

    try:
        assert patch_obj.status_code == 200, "статус код не соответсвует ожидаемому"
        assert patch_obj.json()["name"] == "no_name", "обновление не применено"
    except AssertionError as a:
        print("PATCH request error:", a)

    delete_object(patch_id)


def delete_test():
    obj = post_object()
    obj_id = get_id(obj)

    delete_obj = delete_object(obj_id)
    delete_obj_2 = delete_object(obj_id)

    try:
        assert delete_obj.status_code == 200, "статус код не соответсвует ожидаемому"
        assert delete_obj_2.status_code == 404, "статус код не соответсвует ожидаемому"
    except AssertionError as a:
        print("DELETE request error:", a)


post_test()
put_test()
patch_test()
delete_test()
