import data
import requests
import configuration


def post_create_new_order(order_body):
    return requests.post(
        configuration.SERVER_URL + configuration.API_CREATE_ORDER,
        json=order_body,
        headers=data.headers
    )


def get_find_new_order(track_n):
    return requests.get(
        configuration.SERVER_URL + configuration.API_ORDER_TRACK_NUMBER,
        params={"t": track_n}
    )
