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
    date_price = sorted(date_price, key=lambda x: x[1], reverse=True)

    top_n_sum = sum(float(x[1]) for x in date_price[:n])

    bottom_n_sum = sum(float(x[1]) for x in date_price[-n:])

    print(top_n_sum, bottom_n_sum)

    return top_n_sum - bottom_n_sum


def create_csv_file(data, n, key):
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


def main():
    filepath = os.path.abspath("task_1.csv")
    data = load_csv(filepath)

    print(create_csv_file(data, 31, "dam"))
    print(create_csv_file(data, 31, "rtm"))


if __name__ == "__main__":
    main()
