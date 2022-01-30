from unittest import TestCase, main

from secretsanta.santadraw.santa_draw import SantaDraw
from secretsanta.santadraw.person import Person
from secretsanta.utils.validation import \
    is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family

# Since the Secret Santa Draw is a random assignment, it is hard to validate/verify the pairs.
# Thus, I use ``is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family()`` function
# to validate { Secret Santa : Assignee } pairs without writing all possible cases.


validate_santa_draw = is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family


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
    """Santa Draw with four members for pair assignment"""

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
        family = self.drawer.get_family_members()
        prev_prev_pairs = None
        prev_pairs = None
        for _ in range(100):  # test for 100 times
            santa_pairs = self.drawer.assign_santa_to_everyone()
            self.assertTrue(validate_santa_draw(family, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs


class TestSantaDrawWithManyMembers(TestCase):
    """Santa Draw with more than four members for pair assignment"""

    def test_successful_santa_draw_with_6_members_multiple_times(self):
        """Try pair assignment of Santa Draw with an even number of family members multiple times"""
        drawer = SantaDraw(["m1", "m2", "m3", "m4", "m5", "m6"])
        family = drawer.get_family_members()
        prev_prev_pairs = None
        prev_pairs = None
        for _ in range(100):  # test for 100 times
            santa_pairs = drawer.assign_santa_to_everyone()
            self.assertTrue(validate_santa_draw(family, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs

    def test_successful_santa_draw_with_7_members_multiple_times(self):
        """Try pair assignment of Santa Draw with an odd number of family members multiple times"""
        drawer = SantaDraw(["m1", "m2", "m3", "m4", "m5", "m6", "m7"])
        family = drawer.get_family_members()
        prev_prev_pairs = None
        prev_pairs = None
        for _ in range(100):  # test for 100 times
            santa_pairs = drawer.assign_santa_to_everyone()
            self.assertTrue(validate_santa_draw(family, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs


class TestSantaDrawWithGrowingFamily(TestCase):
    """Santa Draw with growing family members for pair assignment"""

    def test_successful_consecutive_santa_draw(self):
        """Test Santa Draw whether it assigns Secret Santa to a non-immediate family member"""
        drawer = SantaDraw(["orig1", "orig2"])
        family = drawer.get_family_members()

        first_santa_pairs = drawer.assign_santa_to_everyone()
        first_expected = {"orig1": "orig2", "orig2": "orig1"}
        self.assertEqual(first_santa_pairs, first_expected)
        self.assertTrue(validate_santa_draw(family, first_santa_pairs))

        family.add_immediate_family_of_person_with_new_member("orig1", "new11")
        with self.assertRaises(ValueError):  # it is not possible
            drawer.assign_santa_to_everyone()

        family.add_immediate_family_of_person_with_new_member("orig2", "new21")
        second_santa_pairs = drawer.assign_santa_to_everyone()
        second_expected = {"orig1": "new21", "orig2": "new11", "new11": "orig2", "new21": "orig1"}
        self.assertEqual(second_santa_pairs, second_expected)
        self.assertTrue(validate_santa_draw(family, second_santa_pairs, first_santa_pairs))

        family.add_immediate_family_of_person_with_new_member("orig1", "new12")
        family.add_immediate_family_of_person_with_new_member("orig2", "new22")

        prev_prev_pairs = first_santa_pairs
        prev_pairs = second_santa_pairs
        for _ in range(100):  # test for 100 times
            santa_pairs = drawer.assign_santa_to_everyone()
            self.assertTrue(validate_santa_draw(family, santa_pairs, prev_pairs, prev_prev_pairs))
            prev_prev_pairs = prev_pairs
            prev_pairs = santa_pairs


class TestSantaDrawIsValidPairs(TestCase):
    """Test the ``SantaDraw.is_valid_pairs()`` method"""

    def test_is_person_in_last_assignees(self):
        """Test whether santa is not candidate and candidate is not in the santa's last assignees"""
        person1 = Person("Person 1")
        person2 = Person("Person 2")
        person3 = Person("Person 3")
        person4 = Person("Person 4")

        self.assertTrue(SantaDraw.is_valid_pairs(person1, person2))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person3))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person4))

        person1.update_last_assignees_with(person2)
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person2))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person3))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person4))

        person1.update_last_assignees_with(person3)
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person2))
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person3))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person4))

        person1.update_last_assignees_with(person4)
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person2))
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person3))
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person4))

    def test_is_person_in_immediate_family(self):
        """
        Test whether santa is not candidate and candidate is not in the santa's last assignees and candidate is not an
        immediate family member of santa.
        """
        person1 = Person("Person 1")
        person2 = Person("Person 2")
        person3 = Person("Person 3")
        person4 = Person("Person 4")

        self.assertTrue(SantaDraw.is_valid_pairs(person1, person2))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person3))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person4))

        person1.add_immediate_family_with(person2)
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person2))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person3))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person4))

        person1.add_immediate_family_with(person3)
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person2))
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person3))
        self.assertTrue(SantaDraw.is_valid_pairs(person1, person4))

        person1.add_immediate_family_with(person4)
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person2))
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person3))
        self.assertFalse(SantaDraw.is_valid_pairs(person1, person4))


if __name__ == '__main__':
    main()
