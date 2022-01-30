import reprlib

from secretsanta.santadraw.person import Person


class Family:
    """
    ``Family`` class is the sequence protocol.
    ``Family`` class is not hashable since the object is not immutable.
    The members are wrapped in ``Person`` objects with unique names.
    """

    def __init__(self, members=None):
        if members is None:
            self._members = []
        else:
            self._members = list({member if isinstance(member, Person) else Person(member) for member in members})
            for m in self._members:
                self._members.extend(m.get_immediate_family())

    def add_immediate_family_of_person_with_new_member(self, person, new_member):
        """
        This method adds a new member into ``_members`` and delegates the person's ``add_immediate_family_with()``.
        Only if the person is a member of this family, then the add will happen. Otherwise, ignored.

        Family has no ability to know whether an instance of Person has updated their immediate family by themselves.
        Thus, this method must be used if a new member must be in this family.
        """
        for m in self._members:
            if m == person:
                if not isinstance(new_member, Person):
                    new_member = Person(new_member)
                self._members.append(new_member)
                m.add_immediate_family_with(new_member)
                new_member.add_immediate_family_with(person)
                break

    def remove_immediate_family_of_person_with_member(self, person, member):
        """
        This method removes a new member from ``_members`` and delegates the person's ``remove_immediate_family_with()``.
        Only if the person is a member of this family, then the remove will happen. Otherwise, ignored.

        Family has no ability to know whether an instance of Person has updated their immediate family by themselves.
        Thus, this method must be used if a member must be removed from this family.
        """
        valid = False
        for m in self._members:
            if m == person:
                valid = True
                m.remove_immediate_family_with(member)
                break

        if valid:
            for m in self._members:
                if m == member:
                    self._members.remove(m)
                    m.remove_immediate_family_with(person)
                    break

    def __len__(self):
        return len(self._members)

    def __getitem__(self, position):
        return self._members[position]

    def __setitem__(self, position, value):
        if isinstance(value, Person):
            self._members[position] = value
        else:
            self._members[position] = Person(value)

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
