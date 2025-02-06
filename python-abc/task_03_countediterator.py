#!/usr/bin/env python3
class CountedIterator:
    def __init__(self, iterable):
        # Initialize the iterator and the counter.
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        # An iterator must return itself as an iterator.
        return self

    def __next__(self):
        # Attempt to retrieve the next item from the underlying iterator.
        # This will raise StopIteration if the iterator is exhausted.
        item = next(self.iterator)
        # Increment the counter after successfully fetching an item.
        self.count += 1
        return item

    def get_count(self):
        # Return the number of items that have been iterated over so far.
        return self.count
