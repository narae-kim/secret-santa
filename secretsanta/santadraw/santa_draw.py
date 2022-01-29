import random
from datetime import datetime

from secretsanta.santadraw.family import Family
from secretsanta.utils.decorator import synchronized_method, synchronized


class SantaDraw:
    """``SantaDraw`` class assigns a Secret Santa for everyone given a list of all the members of the extended family"""

    def __init__(self, family_members=None):
        if family_members is None:
            self._family_members = Family()
        else:
            self._family_members = Family(family_members)

        self._santa_pairs = {}

    @synchronized_method
    def assign_santa_to_everyone(self, random_seed=datetime.now()):
        """
        Pair assignment requires at least two members (which makes sense). It will raise 'ValueError' if < 2 members.
        To start, it shuffles the members of the family before the pair assignment so that it will give randomness.
        Note: random.shuffle(list) will shuffle the list in-place.
        Then, compare each family member in the previous order and the shuffled family members, and assign pairs.

        :param random_seed: Optional argument to set the random seed for debugging purpose
        :raises ValueError: If the number of family members is less than 2
        """
        if len(self._family_members) < 2:
            raise ValueError("The minimum number of the family for the draw is 2.")
        self._santa_pairs.clear()
        random.seed(random_seed)
        family_temp = list(self._family_members)
        random.shuffle(self._family_members)
        i = len(family_temp)
        for member in self._family_members:
            # this approach would have less time complexity than repetitive random shuffle
            i -= 1
            if member != family_temp[i]:
                self._santa_pairs[member] = family_temp.pop(i)
            elif i != 0:
                self._santa_pairs[member] = family_temp.pop(i - 1)
            else:  # workaround if the last member == family_temp[0], when len(family) == odd numbers
                swap_key = next(iter(self._santa_pairs))
                self._santa_pairs[member] = self._santa_pairs[swap_key]
                self._santa_pairs[swap_key] = member
        return self._santa_pairs

    def get_family_members(self):
        """Getter for the family members that this instance of Santa Draw holds"""
        return self._family_members

    def get_santa_pairs(self):
        """Getter for the latest { Secret Santa : Assignee } pairs"""
        return self._santa_pairs


@synchronized
def santa_draw_fn(family_members, random_seed=datetime.now()):
    """
    This function does exact the same thing as ``assign_santa_to_everyone`` method in ``SantaDraw``.

    Pair assignment requires at least two members (which makes sense). It will raise 'ValueError' if < 2 members.
    To start, it shuffles the members of the family before the pair assignment so that it will give randomness.
    Note: random.shuffle(list) will shuffle the list in-place.
    Then, compare each family member in the previous order and the shuffled family members, and assign pairs.

    :param random_seed: Optional argument to set the random seed for debugging purpose
    :raises ValueError: If the number of family members is less than 2
    """
    if len(family_members) < 2:
        raise ValueError("The minimum number of the family for the draw is 2.")
    santa_pairs = {}
    random.seed(random_seed)
    family_temp = list(family_members)
    random.shuffle(family_members)
    i = len(family_temp)
    for member in family_members:
        # this approach would have less time complexity than repetitive random shuffle
        i -= 1
        if member != family_temp[i]:
            santa_pairs[member] = family_temp.pop(i)
        elif i != 0:
            santa_pairs[member] = family_temp.pop(i - 1)
        else:  # workaround if the last member == family_temp[0], when len(family) == odd numbers
            swap_key = next(iter(santa_pairs))
            santa_pairs[member] = santa_pairs[swap_key]
            santa_pairs[swap_key] = member
    return santa_pairs
