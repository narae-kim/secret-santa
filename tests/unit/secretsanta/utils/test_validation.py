from unittest import TestCase, main

from secretsanta.utils.validation import is_assignee_unique_and_not_themselves_in_pairs, \
    is_distinct_assignee_unique_and_not_in_last_two_pairs, \
    is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family
from secretsanta.santadraw.family import Family


class TestUniqueAssignment(TestCase):
    """Test ``is_assignee_unique_and_not_themselves_in_pairs()`` function"""

    def test_pair_assignment_with_empty_data_structures(self):
        """This is a true test case so it should return True"""
        members = []
        santa_pairs = {}
        self.assertTrue(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs))

    def test_pair_assignment_with_true_case1(self):
        """This is a true test case so it should return True"""
        members = ["m1", "m2", "m3", "m4"]
        santa_pairs = {"m3": "m4", "m4": "m3", "m2": "m1", "m1": "m2"}
        self.assertTrue(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs))

    def test_pair_assignment_with_true_case2(self):
        """There are only two true cases for three members"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs1 = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim'}
        self.assertTrue(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs1))
        santa_pairs2 = {'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee', 'Jung Lee': 'Narae Kim'}
        self.assertTrue(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs2))

    def test_pair_assignment_with_false_case(self):
        """There are six false cases for three members"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs1 = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs1))
        santa_pairs2 = {'Jung Lee': 'Jay Kim', 'Narae Kim': 'Jay Kim', 'Jay Kim': 'Narae Kim'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs2))
        santa_pairs3 = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jay Kim', 'Jay Kim': 'Narae Kim'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs3))
        santa_pairs4 = {'Jung Lee': 'Jay Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs4))
        santa_pairs5 = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs5))
        santa_pairs6 = {'Jung Lee': 'Jay Kim', 'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs6))

    def test_pair_assignment_with_different_len(self):
        """Not all members are assigned so this should be False"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs))

    def test_pair_assignment_with_same_assignee(self):
        """Assignee should be unique so this should be False"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs))

    def test_pair_assignment_with_nonmember_santa(self):
        """Santa must be a member of the family so this should be False"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'NOT_EXIST': 'Jay Kim'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs))

    def test_pair_assignment_with_more_pairs(self):
        """More pairs in ``santa_pairs`` than in ``members`` so it should return False"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim', 'MORE_KYE': 'MORE_VALUE'}
        self.assertFalse(is_assignee_unique_and_not_themselves_in_pairs(members, santa_pairs))

    def test_pair_assignment_with_invalid_pairs_type(self):
        """Invalid type of ``santa_pairs``. It should raise TypeError."""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        invalid_pairs = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        with self.assertRaises(TypeError):
            is_assignee_unique_and_not_themselves_in_pairs(members, invalid_pairs)


class TestUniqueAssignmentNotInPrevTwo(TestCase):
    """Test ``is_distinct_assignee_unique_and_not_in_last_two_pairs()`` function"""

    def test_pair_assignment_with_empty_data_structures(self):
        """This is a true test case so it should return True"""
        members = []
        santa_pairs = {}
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs))

    def test_pair_assignment_with_true_case1(self):
        """This is a true test case so it should return True"""
        members = ["m1", "m2", "m3", "m4"]
        santa_pairs = {"m3": "m4", "m4": "m3", "m2": "m1", "m1": "m2"}
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs))

    def test_pair_assignment_with_true_case2(self):
        """There are only two true cases for three members"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs1 = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim'}
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs1))
        santa_pairs2 = {'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee', 'Jung Lee': 'Narae Kim'}
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs2))

    def test_pair_assignment_with_false_case(self):
        """There are six false cases for three members"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs1 = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs1))
        santa_pairs2 = {'Jung Lee': 'Jay Kim', 'Narae Kim': 'Jay Kim', 'Jay Kim': 'Narae Kim'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs2))
        santa_pairs3 = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jay Kim', 'Jay Kim': 'Narae Kim'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs3))
        santa_pairs4 = {'Jung Lee': 'Jay Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs4))
        santa_pairs5 = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs5))
        santa_pairs6 = {'Jung Lee': 'Jay Kim', 'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs6))

    def test_pair_assignment_with_different_len(self):
        """Not all members are assigned so this should be False"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs))

    def test_pair_assignment_with_same_assignee(self):
        """Assignee should be unique so this should be False"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs))

    def test_pair_assignment_with_nonmember_santa(self):
        """Santa must be a member of the family so this should be False"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'NOT_EXIST': 'Jay Kim'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs))

    def test_pair_assignment_with_more_pairs(self):
        """More pairs in ``santa_pairs`` than in ``members`` so it should return False"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        santa_pairs = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim', 'MORE_KYE': 'MORE_VALUE'}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, santa_pairs))

    def test_pair_assignment_with_invalid_pairs_type(self):
        """Invalid type of ``santa_pairs``. It should raise TypeError"""
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        invalid_pairs = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        with self.assertRaises(TypeError):
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, invalid_pairs)

    def test_successful_pair_assignment_with_one_prev_pairs(self):
        """Test with one valid previous pairs"""
        members = ["m1", "m2", "m3", "m4"]
        first_pairs = {"m1": "m2", "m2": "m1", "m3": "m4", "m4": "m3"}
        second_pairs = {"m1": "m4", "m2": "m3", "m3": "m1", "m4": "m2"}
        third_pairs = {"m1": "m3", "m2": "m4", "m3": "m2", "m4": "m1"}
        fourth_pairs = {"m1": "m3", "m2": "m4", "m3": "m1", "m4": "m2"}
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, first_pairs, second_pairs))
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, first_pairs, third_pairs))
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, first_pairs, fourth_pairs))
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, second_pairs, first_pairs))
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, second_pairs, third_pairs))
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, third_pairs, first_pairs))
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, third_pairs, second_pairs))
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, fourth_pairs, first_pairs))

    def test_failed_pair_assignment_with_one_prev_pair(self):
        """Test with one invalid previous pairs"""
        members = ["m1", "m2", "m3", "m4"]
        second_pairs = {"m1": "m4", "m2": "m3", "m3": "m1", "m4": "m2"}
        third_pairs = {"m1": "m3", "m2": "m4", "m3": "m2", "m4": "m1"}
        fourth_pairs = {"m1": "m3", "m2": "m4", "m3": "m1", "m4": "m2"}
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, second_pairs, fourth_pairs))
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, third_pairs, fourth_pairs))
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, fourth_pairs, second_pairs))
        self.assertFalse(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, fourth_pairs, third_pairs))

    def test_successful_pair_assignment_with_two_prev_pairs(self):
        """Test with two valid previous pairs"""
        members = ["m1", "m2", "m3", "m4"]
        first_pairs = {"m1": "m2", "m2": "m1", "m3": "m4", "m4": "m3"}
        second_pairs = {"m1": "m4", "m2": "m3", "m3": "m1", "m4": "m2"}
        third_pairs = {"m1": "m3", "m2": "m4", "m3": "m2", "m4": "m1"}
        self.assertTrue(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, first_pairs, second_pairs, third_pairs))
        self.assertTrue(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, first_pairs, third_pairs, second_pairs))
        self.assertTrue(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, second_pairs, first_pairs, third_pairs))
        self.assertTrue(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, second_pairs, third_pairs, first_pairs))
        self.assertTrue(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, third_pairs, first_pairs, second_pairs))
        self.assertTrue(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, third_pairs, second_pairs, first_pairs))

    def test_failed_pair_assignment_with_two_prev_pairs(self):
        """Test with two invalid previous pairs"""
        members = ["m1", "m2", "m3", "m4"]
        first_pairs = {"m1": "m2", "m2": "m1", "m3": "m4", "m4": "m3"}
        invalid_pairs1 = {"m1": "m4", "m2": "m3", "m3": "m1", "m4": "m2"}
        invalid_pairs2 = {"m1": "m3", "m2": "m4", "m3": "m1", "m4": "m2"}
        self.assertFalse(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, invalid_pairs1, first_pairs, invalid_pairs2))
        self.assertFalse(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, invalid_pairs1, invalid_pairs2, first_pairs))
        self.assertFalse(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, invalid_pairs2, first_pairs, invalid_pairs1))
        self.assertFalse(
            is_distinct_assignee_unique_and_not_in_last_two_pairs(members, invalid_pairs2, invalid_pairs1, first_pairs))

    def test_successful_consecutive_pair_assignment_with_one_prev_pairs(self):
        """Test with valid previous pairs"""
        members = ["Narae Kim", "Jay Kim", "Jung Lee"]
        pairs1 = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim'}
        pairs2 = {'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee', 'Jung Lee': 'Narae Kim'}

        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, pairs1))
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, pairs2, pairs1))

        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, pairs2))
        self.assertTrue(is_distinct_assignee_unique_and_not_in_last_two_pairs(members, pairs1, pairs2))


# ``validate_part3()`` delegates ``is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family()``
validate_part3 = is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family


class TestUniqueAssignmentNotInPrevTwoNotInImmediateFamily(TestCase):
    """Test ``is_distinct_assignee_unique_and_not_in_last_two_pairs_and_not_in_immediate_family()`` function"""

    def test_pair_assignment_with_empty_data_structures(self):
        """This is a true test case so it should return True"""
        members = []
        santa_pairs = {}
        self.assertTrue(validate_part3(members, santa_pairs))

    def test_pair_assignment_with_true_case1(self):
        """This is a true test case so it should return True"""
        members = Family(["m1", "m2", "m3", "m4"])
        santa_pairs = {"m3": "m4", "m4": "m3", "m2": "m1", "m1": "m2"}
        self.assertTrue(validate_part3(members, santa_pairs))

    def test_pair_assignment_with_true_case2(self):
        """There are only two true cases for three members"""
        members = Family(['Narae Kim', 'Jay Kim', 'Jung Lee'])
        santa_pairs1 = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim'}
        self.assertTrue(validate_part3(members, santa_pairs1))
        santa_pairs2 = {'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee', 'Jung Lee': 'Narae Kim'}
        self.assertTrue(validate_part3(members, santa_pairs2))

    def test_pair_assignment_with_false_case(self):
        """There are six false cases for three members"""
        members = Family(['Narae Kim', 'Jay Kim', 'Jung Lee'])
        santa_pairs1 = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim'}
        self.assertFalse(validate_part3(members, santa_pairs1))
        santa_pairs2 = {'Jung Lee': 'Jay Kim', 'Narae Kim': 'Jay Kim', 'Jay Kim': 'Narae Kim'}
        self.assertFalse(validate_part3(members, santa_pairs2))
        santa_pairs3 = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jay Kim', 'Jay Kim': 'Narae Kim'}
        self.assertFalse(validate_part3(members, santa_pairs3))
        santa_pairs4 = {'Jung Lee': 'Jay Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(validate_part3(members, santa_pairs4))
        santa_pairs5 = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(validate_part3(members, santa_pairs5))
        santa_pairs6 = {'Jung Lee': 'Jay Kim', 'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(validate_part3(members, santa_pairs6))

    def test_pair_assignment_with_different_len(self):
        """Not all members are assigned so this should be False"""
        members = Family(['Narae Kim', 'Jay Kim', 'Jung Lee'])
        santa_pairs = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee'}
        self.assertFalse(validate_part3(members, santa_pairs))

    def test_pair_assignment_with_same_assignee(self):
        """Assignee should be unique so this should be False"""
        members = Family(['Narae Kim', 'Jay Kim', 'Jung Lee'])
        santa_pairs = {'Jung Lee': 'Narae Kim', 'Narae Kim': 'Jung Lee', 'Jay Kim': 'Jung Lee'}
        self.assertFalse(validate_part3(members, santa_pairs))

    def test_pair_assignment_with_nonmember_santa(self):
        """Santa must be a member of the family so this should be False"""
        members = Family(['Narae Kim', 'Jay Kim', 'Jung Lee'])
        santa_pairs = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'NOT_EXIST': 'Jay Kim'}
        self.assertFalse(validate_part3(members, santa_pairs))

    def test_pair_assignment_with_more_pairs(self):
        """More pairs in ``santa_pairs`` than in ``members`` so it should return False"""
        members = Family(['Narae Kim', 'Jay Kim', 'Jung Lee'])
        santa_pairs = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim', 'MORE_KYE': 'MORE_VALUE'}
        self.assertFalse(validate_part3(members, santa_pairs))

    def test_pair_assignment_with_invalid_pairs_type(self):
        """Invalid type of ``santa_pairs``. It should raise TypeError"""
        members = Family(['Narae Kim', 'Jay Kim', 'Jung Lee'])
        invalid_pairs = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        with self.assertRaises(TypeError):
            validate_part3(members, invalid_pairs)

    def test_successful_pair_assignment_with_one_prev_pairs(self):
        """Test with one valid previous pairs"""
        members = Family(["m1", "m2", "m3", "m4"])
        first_pairs = {"m1": "m2", "m2": "m1", "m3": "m4", "m4": "m3"}
        second_pairs = {"m1": "m4", "m2": "m3", "m3": "m1", "m4": "m2"}
        third_pairs = {"m1": "m3", "m2": "m4", "m3": "m2", "m4": "m1"}
        fourth_pairs = {"m1": "m3", "m2": "m4", "m3": "m1", "m4": "m2"}
        self.assertTrue(validate_part3(members, first_pairs, second_pairs))
        self.assertTrue(validate_part3(members, first_pairs, third_pairs))
        self.assertTrue(validate_part3(members, first_pairs, fourth_pairs))
        self.assertTrue(validate_part3(members, second_pairs, first_pairs))
        self.assertTrue(validate_part3(members, second_pairs, third_pairs))
        self.assertTrue(validate_part3(members, third_pairs, first_pairs))
        self.assertTrue(validate_part3(members, third_pairs, second_pairs))
        self.assertTrue(validate_part3(members, fourth_pairs, first_pairs))

    def test_failed_pair_assignment_with_one_prev_pair(self):
        """Test with one invalid previous pairs"""
        members = Family(["m1", "m2", "m3", "m4"])
        second_pairs = {"m1": "m4", "m2": "m3", "m3": "m1", "m4": "m2"}
        third_pairs = {"m1": "m3", "m2": "m4", "m3": "m2", "m4": "m1"}
        fourth_pairs = {"m1": "m3", "m2": "m4", "m3": "m1", "m4": "m2"}
        self.assertFalse(validate_part3(members, second_pairs, fourth_pairs))
        self.assertFalse(validate_part3(members, third_pairs, fourth_pairs))
        self.assertFalse(validate_part3(members, fourth_pairs, second_pairs))
        self.assertFalse(validate_part3(members, fourth_pairs, third_pairs))

    def test_successful_pair_assignment_with_two_prev_pairs(self):
        """Test with two valid previous pairs"""
        members = Family(["m1", "m2", "m3", "m4"])
        first_pairs = {"m1": "m2", "m2": "m1", "m3": "m4", "m4": "m3"}
        second_pairs = {"m1": "m4", "m2": "m3", "m3": "m1", "m4": "m2"}
        third_pairs = {"m1": "m3", "m2": "m4", "m3": "m2", "m4": "m1"}
        self.assertTrue(validate_part3(members, first_pairs, second_pairs, third_pairs))
        self.assertTrue(validate_part3(members, first_pairs, third_pairs, second_pairs))
        self.assertTrue(validate_part3(members, second_pairs, first_pairs, third_pairs))
        self.assertTrue(validate_part3(members, second_pairs, third_pairs, first_pairs))
        self.assertTrue(validate_part3(members, third_pairs, first_pairs, second_pairs))
        self.assertTrue(validate_part3(members, third_pairs, second_pairs, first_pairs))

    def test_failed_pair_assignment_with_two_prev_pairs(self):
        """Test with two invalid previous pairs"""
        members = Family(["m1", "m2", "m3", "m4"])
        first_pairs = {"m1": "m2", "m2": "m1", "m3": "m4", "m4": "m3"}
        invalid_pairs1 = {"m1": "m4", "m2": "m3", "m3": "m1", "m4": "m2"}
        invalid_pairs2 = {"m1": "m3", "m2": "m4", "m3": "m1", "m4": "m2"}
        self.assertFalse(validate_part3(members, invalid_pairs1, first_pairs, invalid_pairs2))
        self.assertFalse(validate_part3(members, invalid_pairs1, invalid_pairs2, first_pairs))
        self.assertFalse(validate_part3(members, invalid_pairs2, first_pairs, invalid_pairs1))
        self.assertFalse(validate_part3(members, invalid_pairs2, invalid_pairs1, first_pairs))

    def test_successful_consecutive_pair_assignment_with_one_prev_pairs(self):
        """Test with valid previous pairs"""
        members = Family(["Narae Kim", "Jay Kim", "Jung Lee"])
        pairs1 = {'Narae Kim': 'Jung Lee', 'Jay Kim': 'Narae Kim', 'Jung Lee': 'Jay Kim'}
        pairs2 = {'Narae Kim': 'Jay Kim', 'Jay Kim': 'Jung Lee', 'Jung Lee': 'Narae Kim'}

        self.assertTrue(validate_part3(members, pairs1))
        self.assertTrue(validate_part3(members, pairs2, pairs1))

        self.assertTrue(validate_part3(members, pairs2))
        self.assertTrue(validate_part3(members, pairs1, pairs2))

    def test_consecutive_pair_assignment_with_growing_family(self):
        """Test validation in terms of the immediate family. This is the key for Part3"""
        members = Family(["orig1", "orig2"])
        first_pairs = {"orig1": "orig2", "orig2": "orig1"}
        self.assertTrue(validate_part3(members, first_pairs))

        members.add_immediate_family_of_person_with_new_member("orig1", "new11")
        members.add_immediate_family_of_person_with_new_member("orig2", "new21")
        second_pairs = {"orig1": "new21", "orig2": "new11", "new11": "orig2", "new21": "orig1"}
        self.assertTrue(validate_part3(members, second_pairs))
        self.assertTrue(validate_part3(members, second_pairs, first_pairs))

        invalid_second_pairs1 = {"orig1": "new11", "orig2": "new21", "new11": "orig2", "new21": "orig1"}
        invalid_second_pairs2 = {"orig1": "new21", "orig2": "new11", "new11": "orig1", "new21": "orig2"}
        self.assertFalse(validate_part3(members, invalid_second_pairs1))
        self.assertFalse(validate_part3(members, invalid_second_pairs1, first_pairs))
        self.assertFalse(validate_part3(members, invalid_second_pairs2))
        self.assertFalse(validate_part3(members, invalid_second_pairs2, first_pairs))


if __name__ == '__main__':
    main()
