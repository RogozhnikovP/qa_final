# Павел Рогожников, 8-а когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


def test_create_new_order():
    response = sender_stand_request.post_create_new_order(data.order_body)
    assert response.status_code == 201


def test_get_order_by_track():
    track_number = sender_stand_request.post_create_new_order(data.order_body).json()["track"]
    response = sender_stand_request.get_find_new_order(track_number)
    assert response.status_code == 200
