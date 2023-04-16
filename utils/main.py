from functions import load_data, sort_payment, data_print

payments_file = 'operations.json'


def main():
    data = load_data(payments_file)
    data = sort_payment(data)

    for i in range(5):
        print(data_print(data[i]))


if __name__ == '__main__':
    main()
