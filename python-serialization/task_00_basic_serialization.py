import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a dictionary and save it as a JSON file.

    Parameters:
    data (dict): Dictionary to serialize.
    filename (str): Output JSON file name.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to '{filename}'.")


def load_and_deserialize(filename):
    """
    Load a JSON file and return its content as a dictionary.

    Parameters:
    filename (str): Input JSON file name.

    Returns:
    dict: Deserialized dictionary.
    """
    with open(filename, 'r') as file:
        return json.load(file)
