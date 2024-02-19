import os
import csv
from datetime import datetime


def read_from_csv_file(filename, location):
    """
        Read from csv file and return data for location.
    """
    csv_path = os.path.abspath(filename)

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        data = [
            entry 
            for entry in reader
            if entry['Settlement Point'].upper() == location
        ]

    return data


def calculate_avg(data, key):
    """
        Calculate Avg.
    """
    return sum(
        float(entry[key])
        for entry in data
    ) / len(data)

def create_task_1(data1, data2):
    """
        Task 1.
    """
    csv_list = []
    idx = 0

    for entry in data1:
        date_time = entry['Delivery Date'] + ' ' + str(int(entry['Delivery Hour']) - 1)
        dam_price = entry['Settlement Point Price']
        rtm_price = calculate_avg(data2[idx: idx+4], 'Settlement Point Price')

        date_obj = datetime.strptime(date_time, '%m/%d/%Y %H')

        csv_dict = {
            'date': datetime.strftime(date_obj, '%Y-%m-%d %H:%M:%S'),
            'dam': f'{float(dam_price):.2f}',
            'rtm': f'{float(rtm_price):.2f}'
        }

        csv_list.append(csv_dict)
        idx += 4

    filepath = os.path.join(os.getcwd(), 'task_1.csv')

    with open(filepath, 'w', encoding='utf-8') as f:
        headers = csv_list[0].keys()
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(csv_list)

    return filepath

def create_task_2(data1, data2):
    """
        Task 2.
    """
    csv_list = []
    idx = 0

    for index, entry in enumerate(data2, start=1):
        date_time = entry['Delivery Date'] + ' ' + str(int(entry['Delivery Hour']) - 1) + ':' + f"{(int(entry['Delivery Interval']) - 1)*15}"
        dam_price = data1[idx]['Settlement Point Price']
        rtm_price = entry['Settlement Point Price']

        date_obj = datetime.strptime(date_time, '%m/%d/%Y %H:%M')

        csv_dict = {
            'date': datetime.strftime(date_obj, '%Y-%m-%d %H:%M:%S'),
            'dam': f'{float(dam_price):.2f}',
            'rtm': f'{float(rtm_price):.2f}'
        }

        csv_list.append(csv_dict)
        
        if index % 4 == 0:
            idx += 1

    filepath = os.path.join(os.getcwd(), 'task_2.csv')

    with open(filepath, 'w', encoding='utf-8') as f:
        headers = csv_list[0].keys()
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(csv_list)

    return filepath



def main():
    """
        Main.
    """
    data1 = read_from_csv_file('DAM_Prices_2022.csv', 'HB_NORTH')
    data2 = read_from_csv_file('RTM_Prices_2022.csv', 'HB_NORTH')

    print(create_task_1(data1, data2))
    print(create_task_2(data1, data2))


if __name__ == '__main__':
    main()