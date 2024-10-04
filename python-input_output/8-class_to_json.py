def class_to_json(obj):
    """Returns a dictionary of an object's serializable attributes."""
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
