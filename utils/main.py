from functions import load_data, sort_payment, data_print


def main():
    data = load_data()
    data = sort_payment(data)

    for i in range(5):
        print(data_print(data[i]))


if __name__ == '__main__':
    main()