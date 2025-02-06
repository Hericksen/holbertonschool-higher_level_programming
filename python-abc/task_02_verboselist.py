#!/usr/bin/env python3
class VerboseList(list):
    def append(self, item):
        # Add the item using the built-in list functionality.
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        # Convert the iterable to a list so we can count the items.
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        # Print the notification before removing the item.
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        # Retrieve the item that will be removed.
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
