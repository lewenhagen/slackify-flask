#!/usr/bin/env python3
"""
Functions file
"""

import csv

def csv_to_dict(file_name="data.csv", deli=";"):
    """
    Read csv with header, create list with dicts. key is header value
    """
    reader = csv.DictReader(open("datafile/" + file_name, 'r', encoding="utf-8"))
    dict_list = []
    headers = []
    for line in reader:
        dict_list.append(line)


    for item in dict_list:
        if item["Förening"] not in headers:
            headers.append(item["Förening"])

    # print(dict_list)
    return {
        "headers": headers,
        "content": dict_list
    }
