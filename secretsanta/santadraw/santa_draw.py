import random
import itertools
from datetime import datetime

from secretsanta.santadraw.family import Family
from secretsanta.utils.synchronized_decorator import synchronized_method, synchronized


class SantaDraw:
    """``SantaDraw`` class assigns a Secret Santa for everyone given a list of all the members of the extended family"""

    def __init__(self, family_members=None):
        self._family_members = Family(family_members)
        self._santa_pairs = {}

    @staticmethod
    def is_valid_pairs(santa, candidate) -> bool:
        """
        ``is_valid_pairs`` returns True if the candidate is valid for the santa. Otherwise, False.
        This method can be overridden when a new requirement or additional constraint comes to Santa Draw.
        This static method also can be a function instead.

        :param santa: This must be an instance of Person
        :param candidate: This can be a name of the person or an instance of Person
        """
        return santa != candidate and not santa.is_person_in_last_assignees(
            candidate) and not santa.is_person_in_immediate_family(candidate)

    def __update_last_assignees(self) -> None:
        """Update the members' last assignees according to the new pairs"""
        for santa, assignee in self._santa_pairs.items():
            santa.update_last_assignees_with(assignee)

    @synchronized_method
    def assign_santa_to_everyone(self, random_seed=datetime.now()):
        """
        Since this method updates attributes of ``self._family_members`` and ``self._santa_pairs``,
        it needs to be thread-safe. Thus, the ``synchronized_method`` decorator is used.
        This pair assignment requires at least two members to assign different people in pairs.
        It will raise 'ValueError' if < 2 members.
        To start, it shuffles the members of the family before the pair assignment so that it will give randomness.
            Note: random.shuffle(list) will shuffle the list in-place.
        Then, validate all possible combination of the family members according to ``self.is_valid_pairs()``
        until it finds validate pairs.

        :param random_seed: Optional argument to set the random seed for debugging purpose
        :raises ValueError: If the number of family members is less than 2 or there is no possible pairs
        """
        if len(self._family_members) < 2:
            # depending on requirements it can raise a customised exception
            raise ValueError("The minimum number of the family for the draw is 2.")
        self._santa_pairs.clear()
        random.seed(random_seed)
        random.shuffle(self._family_members)
        # get possible {santa: [candidates]}
        santa_candidates_pairs = {}
        for member in self._family_members:
            santa_candidates_pairs[member] = [m for m in self._family_members if self.is_valid_pairs(member, m)]
        keys, values = zip(*santa_candidates_pairs.items())
        santa_candidate_combination_gen = (dict(zip(keys, v)) for v in itertools.product(*values))
        for combination_pairs in santa_candidate_combination_gen:
            valid = True
            left_members = set(self._family_members)
            for santa, candidate in combination_pairs.items():  # each possible santa-candidate combination for members
                if candidate in left_members and self.is_valid_pairs(santa, candidate):
                    self._santa_pairs[santa] = candidate
                    left_members.remove(candidate)
                else:
                    valid = False
                    break
            if valid:
                self.__update_last_assignees()
                return self._santa_pairs.copy()
        raise ValueError("This family is invalid to generate secret santa pairs according to the rules.")

    def get_family_members(self):
        """Getter for the family members that this instance of Santa Draw stores"""
        return self._family_members

    def get_santa_pairs(self):
        """Getter for the latest { Secret Santa : Assignee } pairs with a copy of ``_santa_pairs``"""
        return dict(self._santa_pairs)


@synchronized
def draw_secret_santa_pairs(family_members: Family, random_seed=datetime.now()):
    """
    For the reusability of the functionality, this function can be replaced for Santa Draw.
    This function does exact the same thing as ``assign_santa_to_everyone()`` method in ``SantaDraw``.

    Since this function intends to change internal states of ``family_members``, i.e., different orders by shuffling,
    it needs to be thread-safe. Thus, the ``synchronized`` decorator is used.
    This pair assignment requires at least two members to assign different people in pairs.
    It will raise 'ValueError' if < 2 members.
    To start, it shuffles the members of the family before the pair assignment so that it will give randomness.
        Note: random.shuffle(list) will shuffle the list in-place.
    Then, validate all possible combination of the family members according to ``SantaDraw.is_valid_pairs()``
    until it finds validate pairs.
        Note: ``SantaDraw.is_valid_pairs()`` can be a function itself instead of the static method.

    :param family_members: This argument has to be an iterable of Person type, e.g., Family
    :param random_seed: Optional argument to set the random seed for debugging purpose
    :raises ValueError: If the number of family members is less than 2 or there is no possible pairs
    """
    if len(family_members) < 2:
        # depending on requirements it can raise a customised exception
        raise ValueError("The minimum number of the family for the draw is 2.")

    def __update_last_assignees() -> None:
        """Update the members' last assignees according to the new pairs"""
        for santa, assignee in santa_pairs.items():
            santa.update_last_assignees_with(assignee)

    if not isinstance(family_members, Family):
        family_members = Family(family_members)
    santa_pairs = {}
    random.seed(random_seed)
    random.shuffle(family_members)
    # get possible {santa: [candidates]}
    santa_candidates_pairs = {}
    for member in family_members:
        santa_candidates_pairs[member] = [m for m in family_members if SantaDraw.is_valid_pairs(member, m)]
    keys, values = zip(*santa_candidates_pairs.items())
    santa_candidate_combination_gen = (dict(zip(keys, v)) for v in itertools.product(*values))
    for combination_pairs in santa_candidate_combination_gen:
        valid = True
        left_members = set(family_members)
        for santa, candidate in combination_pairs.items():  # each possible santa-candidate combination for members
            if candidate in left_members and SantaDraw.is_valid_pairs(santa, candidate):
                santa_pairs[santa] = candidate
                left_members.remove(candidate)
            else:
                valid = False
                break
        if valid:
            __update_last_assignees()
            return santa_pairs
    raise ValueError("This family is invalid to generate secret santa pairs according to the rules.")
