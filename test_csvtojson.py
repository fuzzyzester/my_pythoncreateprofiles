import csv
import json

def test_csv_has_12_columns():
    with open('profiles1.csv', newline='', encoding='utf-8') as csvf:
        reader = csv.reader(csvf)
        headers = next(reader)
        assert len(headers) == 12

def test_csv_has_900_plus_rows():
    with open('profiles1.csv', newline='', encoding='utf-8') as csvf:
        reader = csv.reader(csvf)
        rows = list(reader)
        assert len(rows) >= 901  # headers + 900 rows

def test_json_has_all_properties():
    with open('data.json', encoding='utf-8') as jsonf:
        data = json.load(jsonf)
        assert len(data) >= 900
        required_keys = data[0].keys()
        for entry in data:
            for key in required_keys:
                assert key in entry

def test_json_has_900_plus_rows():
    with open('data.json', encoding='utf-8') as jsonf:
        data = json.load(jsonf)
        assert len(data) >= 900
