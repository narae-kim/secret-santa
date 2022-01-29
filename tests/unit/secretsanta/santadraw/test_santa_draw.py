from unittest import TestCase, main

from secretsanta.santadraw.santa_draw import SantaDraw
from secretsanta.utils.validation import is_distinct_assignee_unique_and_not_in_last_two_pairs

# Since the Secret Santa Draw is a random assignment, it is hard to validate/verify the pairs.
# Thus, I use ``is_distinct_assignee_unique_and_not_in_last_two_pairs`` function to validate { Secret Santa : Assignee }
# pairs without writing all possible cases.

# RANDOM_SEED = 123

validate_santa_draw = is_distinct_assignee_unique_and_not_in_last_two_pairs


class TestSantaDrawWithLessThanTwoMembers(TestCase):
    """Santa Draw requires at least two members for pair assignment which makes sense"""

    def test_no_members(self):
        """Santa Draw cannot assign { Secret Santa : Assignee } pairs with no members. It will raise 'ValueError'"""
        drawer = SantaDraw()
        with self.assertRaises(ValueError):
            drawer.assign_santa_to_everyone()

    def test_one_member(self):
        """Santa Draw cannot assign { Secret Santa : Assignee } pairs with one member. It will raise 'ValueError'"""
        drawer = SantaDraw(["ALONE"])
        with self.assertRaises(ValueError):
            drawer.assign_santa_to_everyone()


class TestSantaDrawWithThreeMembers(TestCase):
    """Santa Draw with three members for pair assignment"""

    def setUp(self) -> None:
        """Each test case will have those members for Santa Draw"""
        self.members = ["Narae Kim", "Jay Kim", "Jung Lee"]
        self.drawer = SantaDraw(self.members)

    def test_get_family_members(self):
        """Test the getter of family members"""
        self.assertEqual(self.drawer.get_family_members(), self.members)

    def test_get_santa_pairs(self):
        """Test the getter for the latest { Secret Santa : Assignee } pairs"""
        self.assertEqual(self.drawer.assign_santa_to_everyone(), self.drawer.get_santa_pairs())

    def test_successful_santa_draw(self):
        """There are only two true cases for three members"""
        expected1 = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim'}
        expected2 = {'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee', 'Jung Lee': 'Narae Kim'}

        santa_pairs = self.drawer.assign_santa_to_everyone()
        self.assertTrue(santa_pairs == expected1 or santa_pairs == expected2)
        self.assertTrue(validate_santa_draw(self.drawer.get_family_members(), santa_pairs))

    def test_failed_santa_draw_at_third_times(self):
        """There are only two true cases for three members and no possible pairs on the third year"""
        expected1 = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim'}
        expected2 = {'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee', 'Jung Lee': 'Narae Kim'}

        # first time
        first_santa_pairs = self.drawer.assign_santa_to_everyone()
        self.assertTrue(first_santa_pairs == expected1 or first_santa_pairs == expected2)
        self.assertTrue(validate_santa_draw(self.drawer.get_family_members(), first_santa_pairs))

        # second time
        second_santa_pairs = self.drawer.assign_santa_to_everyone()
        self.assertTrue(second_santa_pairs == expected1 or second_santa_pairs == expected2)
        self.assertTrue(validate_santa_draw(self.drawer.get_family_members(), second_santa_pairs, first_santa_pairs))

        # third time
        with self.assertRaises(ValueError):
            self.drawer.assign_santa_to_everyone()


class TestSantaDrawWithFourMembers(TestCase):
    def setUp(self) -> None:
        """Each test case will have those members for Santa Draw"""
        self.members = ["m1", "m2", "m3", "m4"]
        self.drawer = SantaDraw(self.members)

    def test_get_family_members(self):
        """Test the getter of family members"""
        self.assertEqual(self.drawer.get_family_members(), self.members)

    def test_get_santa_pairs(self):
        """Test the getter for the latest { Secret Santa : Assignee } pairs"""
        self.assertEqual(self.drawer.assign_santa_to_everyone(), self.drawer.get_santa_pairs())

    def test_successful_santa_draw(self):
        """The pair assignment will always succeed"""
        santa_pairs = self.drawer.assign_santa_to_everyone()
        self.assertTrue(validate_santa_draw(self.drawer.get_family_members(), santa_pairs))

    def test_successful_santa_draw_multiple_times(self):
        """Try pair assignment of Santa Draw multiple times"""
        prev_prev_pairs = None
        prev_pairs = None
        for _ in range(100):  # test for 100 times
            santa_pairs = self.drawer.assign_santa_to_everyone()
            self.assertTrue(validate_santa_draw(self.members, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs


class TestSantaDrawWithManyMembers(TestCase):
    def test_successful_santa_draw_with_6_members_multiple_times(self):
        """Try pair assignment of Santa Draw with an even number of family members multiple times"""
        members = ["m1", "m2", "m3", "m4", "m5", "m6"]
        drawer = SantaDraw(members)
        prev_prev_pairs = None
        prev_pairs = None
        for _ in range(100):  # test for 100 times
            santa_pairs = drawer.assign_santa_to_everyone()
            self.assertTrue(validate_santa_draw(members, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs

    def test_successful_santa_draw_with_7_members_multiple_times(self):
        """Try pair assignment of Santa Draw with an odd number of family members multiple times"""
        members = ["m1", "m2", "m3", "m4", "m5", "m6", "m7"]
        drawer = SantaDraw(members)
        prev_prev_pairs = None
        prev_pairs = None
        for _ in range(100):  # test for 100 times
            santa_pairs = drawer.assign_santa_to_everyone()
            self.assertTrue(validate_santa_draw(members, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs


if __name__ == '__main__':
    main()
