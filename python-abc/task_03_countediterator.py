class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterator)  # Get the next item from the iterator
        self.counter += 1           # Increment the counter
        return item                 # Return the item
