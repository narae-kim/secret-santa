from unittest import TestCase, main

from secretsanta.santadraw.santa_draw import draw_secret_santa_pairs
from secretsanta.santadraw.family import Family
from secretsanta.utils.validation import \
    is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family

# Since the Secret Santa Draw is a random assignment, it is hard to validate/verify the pairs.
# Thus, I use ``is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family()`` function to
# validate { Secret Santa : Assignee } pairs without writing all possible cases.


validate_santa_draw = is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family


class TestSantaDrawFnWithLessThanTwoMembers(TestCase):
    """Santa Draw requires at least two members for pair assignment which makes sense"""

    def test_no_members(self):
        """Santa Draw cannot assign { Secret Santa : Assignee } pairs with no members. It will raise 'ValueError'"""
        with self.assertRaises(ValueError):
            draw_secret_santa_pairs([])

    def test_one_member(self):
        """Santa Draw cannot assign { Secret Santa : Assignee } pairs with one member. It will raise 'ValueError'"""
        with self.assertRaises(ValueError):
            draw_secret_santa_pairs(["ALONE"])


class TestSantaDrawWithThreeMembers(TestCase):
    """Santa Draw with three members for pair assignment"""

    def setUp(self) -> None:
        """Each test case will have those members for Santa Draw"""
        self.members = Family(["Narae Kim", "Jay Kim", "Jung Lee"])

    def test_successful_santa_draw(self):
        """There are only two true cases for three members"""
        expected1 = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim'}
        expected2 = {'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee', 'Jung Lee': 'Narae Kim'}

        santa_pairs = draw_secret_santa_pairs(self.members)
        self.assertTrue(santa_pairs == expected1 or santa_pairs == expected2)
        self.assertTrue(validate_santa_draw(self.members, santa_pairs))

    def test_failed_santa_draw_at_third_times(self):
        """There are only two true cases for three members and no possible pairs on the third year"""
        expected1 = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim'}
        expected2 = {'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee', 'Jung Lee': 'Narae Kim'}

        # first time
        first_santa_pairs = draw_secret_santa_pairs(self.members)
        self.assertTrue(first_santa_pairs == expected1 or first_santa_pairs == expected2)
        self.assertTrue(validate_santa_draw(self.members, first_santa_pairs))

        # second time
        second_santa_pairs = draw_secret_santa_pairs(self.members)
        self.assertTrue(second_santa_pairs == expected1 or second_santa_pairs == expected2)
        self.assertTrue(validate_santa_draw(self.members, second_santa_pairs, first_santa_pairs))

        # third time
        with self.assertRaises(ValueError):
            draw_secret_santa_pairs(self.members)


class TestSantaDrawWithFourMembers(TestCase):
    def setUp(self) -> None:
        """Each test case will have those members for Santa Draw"""
        self.members = Family(["m1", "m2", "m3", "m4"])

    def test_successful_santa_draw(self):
        """The pair assignment will always succeed"""
        santa_pairs = draw_secret_santa_pairs(self.members)
        self.assertTrue(validate_santa_draw(self.members, santa_pairs))

    def test_successful_santa_draw_multiple_times(self):
        """Try pair assignment of Santa Draw multiple times"""
        prev_prev_pairs = None
        prev_pairs = None
        for _ in range(100):  # test for 100 times
            santa_pairs = draw_secret_santa_pairs(self.members)
            self.assertTrue(validate_santa_draw(self.members, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs


class TestSantaDrawWithManyMembers(TestCase):
    def test_successful_santa_draw_with_6_members_multiple_times(self):
        """Try pair assignment of Santa Draw with an even number of family members multiple times"""
        members = Family(["m1", "m2", "m3", "m4", "m5", "m6"])
        prev_prev_pairs = None
        prev_pairs = None
        for _ in range(100):  # test for 100 times
            santa_pairs = draw_secret_santa_pairs(members)
            self.assertTrue(validate_santa_draw(members, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs

    def test_successful_santa_draw_with_7_members_multiple_times(self):
        """Try pair assignment of Santa Draw with an odd number of family members multiple times"""
        members = Family(["m1", "m2", "m3", "m4", "m5", "m6", "m7"])
        prev_prev_pairs = None
        prev_pairs = None
        for _ in range(100):  # test for 100 times
            santa_pairs = draw_secret_santa_pairs(members)
            self.assertTrue(validate_santa_draw(members, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs


class TestSantaDrawWithGrowingFamily(TestCase):
    """Santa Draw with growing family members for pair assignment"""

    def test_successful_consecutive_santa_draw(self):
        """Test Santa Draw whether it assigns Secret Santa to a non-immediate family member"""
        family = Family(["orig1", "orig2"])

        first_santa_pairs = draw_secret_santa_pairs(family)
        first_expected = {"orig1": "orig2", "orig2": "orig1"}
        self.assertEqual(first_santa_pairs, first_expected)
        self.assertTrue(validate_santa_draw(family, first_santa_pairs))

        family.add_immediate_family_of_person_with_new_member("orig1", "new11")
        with self.assertRaises(ValueError):  # it is not possible
            draw_secret_santa_pairs(family)

        family.add_immediate_family_of_person_with_new_member("orig2", "new21")
        second_santa_pairs = draw_secret_santa_pairs(family)
        second_expected = {"orig1": "new21", "orig2": "new11", "new11": "orig2", "new21": "orig1"}
        self.assertEqual(second_santa_pairs, second_expected)
        self.assertTrue(validate_santa_draw(family, second_santa_pairs, first_santa_pairs))

        family.add_immediate_family_of_person_with_new_member("orig1", "new12")
        family.add_immediate_family_of_person_with_new_member("orig2", "new22")

        prev_prev_pairs = first_santa_pairs
        prev_pairs = second_santa_pairs
        for _ in range(100):  # test for 100 times
            santa_pairs = draw_secret_santa_pairs(family)
            self.assertTrue(validate_santa_draw(family, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs


if __name__ == '__main__':
    main()
