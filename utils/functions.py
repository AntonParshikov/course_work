import json

payments_file = 'operations.json'


def load_data():
    with open(payments_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def sort_payment(data):
    data = [pay for pay in data if pay.get('state') == 'EXECUTED']
    data = sorted(data, key=lambda item: item['date'], reverse=True)
    return data


def data_print(item):
    correct_format = format_date(item.get("date"))

    return f'{correct_format} {item.get("description")}\n' \
           f'{item.get("from")} => {item.get("to")}\n' \
           f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'


def format_date(date):
    str_date = date[:10].split('-')
    return '.'.join(reversed(str_date))


if __name__ == '__main__':
    payments_data = load_data()
    print(sort_payment(payments_data))
