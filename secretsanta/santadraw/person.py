from collections import deque


class Person:
    """
    ``Person`` class is hashable based on the attribute ``name``. Thus, ``name`` must be immutable.
    In this project, I made an assumption that each Person will have a unique name.
    Each person instance holds ``_immediate_family`` as a set type and it can be updated by
    ``add_immediate_family_with()`` and ``remove_immediate_family_with()``.

    To allow the same name people, I could have introduced personal ID by a class attribute, e.g., ``count``.
    In that case, __hash__ and __eq__ methods need to be updated accordingly.
    """

    def __init__(self, name, immediate_family=None):
        self.__name = name
        self._last_assignees = deque(maxlen=2)  # only holds last two assignees
        if immediate_family is None:
            self._immediate_family = set()
        else:
            self._immediate_family = {member if isinstance(member, Person) else Person(member) for member in
                                      immediate_family}

    def is_person_in_immediate_family(self, person) -> bool:
        """
        Return True if the person is in the immediate family, ``_immediate_family``, of this person.
        Otherwise, return False.
        """
        return person in self._immediate_family

    def add_immediate_family_with(self, person) -> None:
        """Add the person in the immediate family, ``_immediate_family``, as an instance of ``Person``"""
        if isinstance(person, Person):
            self._immediate_family.add(person)
        else:
            self._immediate_family.add(Person(person))

    def remove_immediate_family_with(self, person) -> None:
        """
        Remove the person from the immediate family, ``_immediate_family``.
        If the person does not exist, nothing happens (no exception).
        """
        if isinstance(person, Person):
            self._immediate_family.discard(person)
        else:
            self._immediate_family.discard(Person(person))

    def get_immediate_family(self):
        """Getter for the immediate family. Return a copy of ``self._immediate_family``"""
        return set(self._immediate_family)

    def is_person_in_last_assignees(self, person) -> bool:
        """
        Return True if the person is in ``self._last_assignees``.
        In other words, return True if the person was this person's assignee in the last two times.
        Otherwise, return False.
        """
        return person in self._last_assignees

    def update_last_assignees_with(self, person) -> None:
        """
        Add the person in ``self._last_assignees``.
        In other words, update the queue with the person once the person is assigned to this person.
        """
        self._last_assignees.append(person)

    @property
    def name(self):
        """The attribute ``name`` is read-only"""
        return self.__name

    def __repr__(self):
        return "{}({})".format(type(self).__name__, repr(self.name))

    def __str__(self):
        return str(self.name)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        """``Person`` compares the name of self and str(other) only"""
        return str(self) == str(other)
