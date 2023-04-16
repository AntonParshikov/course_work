from utils.functions import sort_payment, load_data, format_date, card_masking, data_print


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


def test_format_date():
    assert format_date("2018-06-12T07:17:01.311610") == "12.06.2018"
    assert format_date("2019-07-12T08:11:47.735774") == "12.07.2019"


def test_card_masking():
    assert card_masking("Счет 90562872508279542248") == "Счет **2248"
    assert card_masking("MasterCard 8532498887072395") == "MasterCard 8532 49** **** 2395"
    assert card_masking("МИР 8201420097886664") == "МИР 8201 42** **** 6664"


def test_data_print():
    dict_1 = {
        "id": 988276204,
        "state": "EXECUTED",
        "date": "2018-02-22T00:40:19.984219",
        "operationAmount": {
            "amount": "71771.90",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 4956649687637418",
        "to": "Счет 90562872508279542248"
    }
    dict_2 = {
        "id": 172864002,
        "state": "EXECUTED",
        "date": "2018-12-28T23:10:35.459698",
        "operationAmount": {
            "amount": "49192.52",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 96231448929365202391"
    }

    str_1 = '22.02.2018 Перевод организации\n' \
            'MasterCard 4956 64** **** 7418 -> Счет **2248\n' \
            '71771.90 USD\n'
    str_2 = '28.12.2018 Открытие вклада\n' \
            'Счет **2391\n' \
            '49192.52 USD\n'

    assert data_print(dict_1) == str_1
    assert data_print(dict_2) == str_2
