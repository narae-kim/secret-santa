# Since the Secret Santa Draw is a random assignment, it is hard to validate/verify the pairs.
# Thus, this function will help us to validate { Secret Santa : Assignee } pairs without writing all possible cases.
def is_assignee_unique_and_not_themselves_in_pairs(santas, pairs: dict) -> bool:
    """
    Given the iterable ``santas``, validate the given ``pairs`` have random assignment to each other.
    If the unique keys of ``pairs`` are same as ``inputs`` and each key has a unique value, not themselves,
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
