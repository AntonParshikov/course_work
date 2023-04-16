from utils.functions import sort_payment


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

