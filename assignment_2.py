"""
    Module name :- assignment_2
"""

import csv
from datetime import datetime
import os


def load_csv(filepath):
    """
    Load CSV file.
    """
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = list(csv.DictReader(f))

    return reader


def tbn_revenue(date_price, n):
    """
    Find TBn revenue.
    """
    date_price = sorted(date_price, key=lambda x: float(x[1]), reverse=True)

    top_n_sum = sum(float(x[1]) for x in date_price[:n])
    bottom_n_sum = sum(float(x[1]) for x in date_price[-n:])

    return top_n_sum - bottom_n_sum


def modified_tbn_revenue(date_price, n):
    """
    Modified TBn revenue.
    """

    max_list, min_list = [], []
    maximum = 0
    prices = [float(entry[1]) for entry in date_price]
    start = 2

    while len(max_list) < n:
        maximum, idx = 0, 0
        for i in range(start, len(prices)):
            price = prices[i]
            if price > maximum and price not in max_list:
                maximum = price
                idx = i

        sort_price = sorted(prices[:idx])

        if maximum > float(sort_price[0]):
            for price in sort_price:
                if price not in min_list:
                    max_list.append(maximum)
                    min_list.append(price)
                    print(idx)
                    break
        else:
            start += 1

    return sum(max_list) - sum(min_list) if max_list and min_list else 0


def create_csv_file(data, n, key):
    """
    Create Modified CSV file with date and price.
    """
    key_data = []
    idx = 0

    for _ in range(n):
        dataframe = []

        for _ in range(24):
            dataframe.append([data[idx]["date"], data[idx][key]])
            idx += 1

        date_obj = datetime.strptime(dataframe[0][0], "%Y-%m-%d %H:%M:%S")

        key_dict = {
            "date": datetime.strftime(date_obj, "%Y-%m-%d"),
            "price": f"{tbn_revenue(dataframe, 2):.2f}",
        }

        key_data.append(key_dict)

    filepath = os.path.join(os.getcwd(), f"{key}_tb2.csv")
    with open(filepath, "w", encoding="utf-8") as f:
        headers = key_data[0].keys()
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(key_data)

    return filepath


def create_modified_csv_file(data, n, key):
    """
    Create CSV file with date and price.
    """
    key_data = []
    idx = 0

    for _ in range(n):
        dataframe = []

        for _ in range(24):
            dataframe.append([data[idx]["date"], data[idx][key]])
            idx += 1

        date_obj = datetime.strptime(dataframe[0][0], "%Y-%m-%d %H:%M:%S")

        key_dict = {
            "date": datetime.strftime(date_obj, "%Y-%m-%d"),
            "price": f"{modified_tbn_revenue(dataframe, 2):.2f}",
        }

        key_data.append(key_dict)

    filepath = os.path.join(os.getcwd(), f"modified_{key}_tb2.csv")
    with open(filepath, "w", encoding="utf-8") as f:
        headers = key_data[0].keys()
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(key_data)

    return filepath


def main():
    """
    main().
    """
    filepath = os.path.abspath("task_1.csv")
    data = load_csv(filepath)

    print(create_csv_file(data, 31, "dam"))
    print(create_csv_file(data, 31, "rtm"))

    print(create_modified_csv_file(data, 31, "dam"))


if __name__ == "__main__":
    main()
