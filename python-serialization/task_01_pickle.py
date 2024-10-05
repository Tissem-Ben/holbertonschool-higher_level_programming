import pickle


class CustomObject:
    def __init__(self, name, age, student):
        """
        Initialize CustomObject with name, age, and student attributes.
        """
        self.name = name
        self.age = age
        self.student = student

    def display(self):
        """Print object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.student}")

    def serialize(self, file):
        """
        Serialize the object and save to a file.

        Parameters:
        file (str): File to save the object.
        """
        try:
            with open(file, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error saving object: {e}")

    @classmethod
    def deserialize(cls, file):
        """
        Load and deserialize an object from a file.

        Parameters:
        file (str): File to load from.

        Returns:
        CustomObject or None if an error occurs.
        """
        try:
            with open(file, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error loading object: {e}")
            return None
