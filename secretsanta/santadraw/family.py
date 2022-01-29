import reprlib


class Family:
    """
    ``Family`` class is the sequence protocol.
    ``Family`` class is not hashable since the object is not immutable.
    The members only have unique names.
    """

    def __init__(self, members=None):
        if members is None:
            self._members = []
        else:
            self._members = list(set(members))

    def __len__(self):
        return len(self._members)

    def __getitem__(self, position):
        return self._members[position]

    def __setitem__(self, position, value):
        self._members[position] = value

    def __delitem__(self, position):
        del self._members[position]

    def __iter__(self):
        return (member for member in self._members)

    def __repr__(self):
        class_name = type(self).__name__
        if not self._members:
            return "{}()".format(class_name)
        else:
            members = reprlib.repr([str(member) for member in self])
            return "{}({})".format(class_name, members)

    def __eq__(self, other):
        """Based on the assumption, this logic makes sense"""
        return len(self) == len(other) and all(a in other and b in self for a, b in zip(self, other))
