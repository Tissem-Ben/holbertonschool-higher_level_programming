import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to JSON format and write to data.json.

    Parameters:
    filename (str): The name of the CSV file to convert.

    Returns:
    bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
