import json


def load_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def sort_payment(data):
    data = [pay for pay in data if pay.get('state') == 'EXECUTED']
    data = sorted(data, key=lambda item: item['date'], reverse=True)
    return data


def data_print(item):
    correct_format = format_date(item.get("date"))

    if item.get("from"):
        from_ = card_masking(item.get("from")) + ' -> '
    else:
        from_ = ''

    return f'{correct_format} {item.get("description")}\n' \
           f'{from_}{card_masking(item.get("to"))}\n' \
           f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'


def format_date(date):
    str_date = date[:10].split('-')
    return '.'.join(reversed(str_date))


def card_masking(card):
    card = card.split(' ')
    if card[0] == 'Счет':
        return f'{card[0]} **{card[-1][-4:]}'

    return f'{" ".join(card[:-1])} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}'



