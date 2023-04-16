from utils.functions import sort_payment, load_data


def test_load_data():
    list_ = [
        {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": "90582.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        }
    ]
    assert load_data('test.json') == list_


def test_sort_payment():
    list_ = [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2019-08-19T04:27:37.904916"
        },
        {
            "id": 863064926,
            "state": "OPEN",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2021-04-14T19:35:28.978265"
        }
    ]

    sorted_list = [
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2021-04-14T19:35:28.978265"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2019-08-19T04:27:37.904916"
        }

    ]

    assert sort_payment(list_) == sorted_list
