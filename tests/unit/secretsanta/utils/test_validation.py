from unittest import TestCase, main

from secretsanta.utils.validation import is_assignee_unique_and_not_themselves_in_pairs


class TestUniqueAssignment(TestCase):
    """Test ``is_assignee_unique_and_not_themselves_in_pairs`` function"""

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
        """
        Invalid type of ``santa_pairs``. It should raise TypeError.
        """
        members = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        invalid_pairs = ['Narae Kim', 'Jay Kim', 'Jung Lee']
        with self.assertRaises(TypeError):
            is_assignee_unique_and_not_themselves_in_pairs(members, invalid_pairs)


if __name__ == '__main__':
    main()
