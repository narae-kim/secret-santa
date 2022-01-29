# Since the Secret Santa Draw is a random assignment, it is hard to validate/verify the pairs.
# Thus, these functions will help us to validate { Secret Santa : Assignee } pairs without writing all possible cases.


def is_assignee_unique_and_not_themselves_in_pairs(santas, pairs: dict) -> bool:
    """
    Given the iterable ``santas``, validate the given ``pairs`` have random assignment to each other.
    If the unique keys of ``pairs`` are same as ``santas`` and each key has a unique value, not themselves,
    from ``santas``, then return True. Otherwise, return False.
    """
    if len(santas) != len(pairs):
        return False
    covered_members = set()
    for santa in santas:
        try:
            if pairs[santa] == santa or pairs[santa] not in santas:
                return False
            covered_members.add(pairs[santa])
        except KeyError:
            return False
    return len(covered_members) == len(santas)


def is_distinct_assignee_unique_and_not_in_last_two_pairs(santas, pairs: dict, prev_pairs1: dict = None,
                                                          prev_pairs2: dict = None) -> bool:
    """
    Given the iterable ``santas`` with ``pairs`` and two optional previous pairs, ``prev_pairs1`` and ``prev_pairs2``,
    validate the given ``pairs`` have random assignment to each other and not overlapped with the previous pairs.
    If the unique keys of ``pairs`` are same as ``santas`` and each key has a unique value, not themselves,
    from ``santas`` and not overlapped with the two previous pairs, then return True. Otherwise, return False.
    """
    if len(santas) != len(pairs):
        return False
    if prev_pairs1 is None:
        prev_pairs1 = {}
    if prev_pairs2 is None:
        prev_pairs2 = {}
    # merge two previous pairs
    combined_prev_pairs = {}
    for prev_pair in (prev_pairs1, prev_pairs2):
        for k, v in prev_pair.items():
            combined_prev_pairs.setdefault(k, []).extend([v])
    covered_members = set()
    for santa in santas:
        try:
            if pairs[santa] == santa or pairs[santa] not in santas:
                return False
            if santa in combined_prev_pairs.keys() and pairs[santa] in combined_prev_pairs[santa]:
                return False
            covered_members.add(pairs[santa])
        except KeyError:
            return False
    return len(covered_members) == len(santas)
