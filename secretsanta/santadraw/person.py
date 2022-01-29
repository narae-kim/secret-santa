from collections import deque


class Person:
    """
    `Person` class is hashable based on the attribute ``name``. Thus, ``name`` must be immutable.
    In this project, I made an assumption that each Person will have a unique name.

    To allow the same name people, I could have introduced personal ID by a class attribute, e.g., ``count``.
    In that case, __hash__ and __eq__ methods need to be updated accordingly.
    """

    # count = 1

    def __init__(self, name):
        self.__name = name
        self._last_assignees = deque(maxlen=2)  # only holds last two assignees
        # self.__id = Person.count
        # Person.count += 1

    def is_person_in_last_assignees(self, person) -> bool:
        """
        Return True if the person is in ``self._last_assignees``.
        In other words, return True if the person was this person's assignee in the last two years.
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

    # @property
    # def id(self):
    #     return self.__id

    def __repr__(self):
        return "{}({})".format(type(self).__name__, repr(self.name))

    def __str__(self):
        return str(self.name)

    def __hash__(self):
        # return hash(self.name) ^ hash(self.id)
        return hash(self.name)

    def __eq__(self, other):
        """``Person`` compares the name of self and other only"""
        return str(self) == str(other)
