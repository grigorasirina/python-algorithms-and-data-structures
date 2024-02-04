# Define the CustomList class to mimic Python's built-in list functionality
class CustomList:
    def __init__(self, iterable=None):
        """Initialize the CustomList with items from an iterable or an empty list if none is provided."""
        self.items = list(iterable) if iterable else []

    def append(self, item):
        """Append an item to the end of the list."""
        self.items.append(item)

    def insert(self, index, item):
        """Insert an item at a given position."""
        self.items.insert(index, item)

    def extend(self, iterable):
        """Extend the list by appending all items from the iterable."""
        self.items.extend(iterable)

    def remove(self, item):
        """Remove the first occurrence of a value."""
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError("Item not found in list.")

    def pop(self, index=-1):
        """Remove the item at the given position in the list and return it."""
        if -len(self.items) <= index < len(self.items):
            return self.items.pop(index)
        else:
            raise IndexError("Index out of range.")

    def clear(self):
        """Remove all items from the list."""
        self.items.clear()

    def index(self, item, start=0, end=None):
        """Return the index of the first occurrence of a value."""
        end = end if end is not None else len(self.items)
        for i in range(start, end):
            if self.items[i] == item:
                return i
        raise ValueError("Item not found in list.")

    def count(self, item):
        """Return the number of times a value appears in the list."""
        return self.items.count(item)

    def sort(self, key=None, reverse=False):
        """Sort the items of the list in place."""
        self.items.sort(key=key, reverse=reverse)

    def reverse(self):
        """Reverse the elements of the list in place."""
        self.items.reverse()

    def copy(self):
        """Return a shallow copy of the list."""
        return CustomList(self.items)

    def __len__(self):
        """Return the number of items in the list."""
        return len(self.items)

    def __getitem__(self, index):
        """Retrieve an item or a slice from the list."""
        return self.items[index]

    def __setitem__(self, index, value):
        """Set an item or a slice of the list."""
        self.items[index] = value

    def __delitem__(self, index):
        """Remove an item or a slice from the list."""
        del self.items[index]

    def __iter__(self):
        """Return an iterator over the list's items."""
        return iter(self.items)

    def __str__(self):
        """Return a string representation of the list for debugging."""
        return str(self.items)

    def __repr__(self):
        """Return an official string representation of the list."""
        return f"CustomList({self.items})"

# Example usage of the CustomList class
if __name__ == "__main__":
    cl = CustomList([1, 2, 3])
    cl.append(4)
    print(f"After append: {cl}")
    cl.insert(1, 5)
    print(f"After insert: {cl}")
    cl.extend([6, 7])
    print(f"After extend: {cl}")
    cl.remove(5)
    print(f"After remove: {cl}")
    popped_item = cl.pop()
    print(f"After pop: {cl}, Popped item: {popped_item}")
    print(f"List length: {len(cl)}")
    cl.sort(reverse=True)
    print(f"After sort: {cl}")
    cl.reverse()
    print(f"After reverse: {cl}")
    cl_copy = cl.copy()
    print(f"Copy of list: {cl_copy}")
    print(f"Index of item 3: {cl.index(3)}")
    print(f"Count of item 3: {cl.count(3)}")

