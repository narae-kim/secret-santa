from unittest import TestCase, main

from secretsanta.santadraw.family import Family
from secretsanta.santadraw.person import Person


class TestDefaultFamilyMember(TestCase):
    """Test ``Family`` when members are not given"""

    def setUp(self) -> None:
        """Instantiate ``Family`` class without any arguments"""
        self.family = Family()

    def test_repr_method(self):
        """The repr of ``Family`` should guide developers on how to replicate the instance"""
        self.assertEqual(repr(self.family), "Family()")

    def test_member_not_in_family(self):
        """No member is in the family so this should return False"""
        self.assertFalse("Julia" in self.family)

    def test_len_family(self):
        """This should return the number of members in the family"""
        self.assertEqual(len(self.family), 0)


class TestNonDefaultFamilyMembers(TestCase):
    """Test ``Family`` with a list of members"""

    def setUp(self) -> None:
        """Instantiate ``Family`` class with two members"""
        self.family = Family(["Jay Kim", "Jung Lee"])

    def test_repr_method(self):
        """The repr of ``Family`` should guide developers on how to replicate the instance"""
        expected1 = "Family(['Jay Kim', 'Jung Lee'])"
        expected2 = "Family(['Jung Lee', 'Jay Kim'])"
        self.assertTrue(repr(self.family) == expected1 or repr(self.family) == expected2)

    def test_repr_method_with_person(self):
        """The repr of ``Family`` should guide developers on how to replicate the instance"""
        persons_family = Family([Person("Jay Kim"), Person("Jung Lee")])
        self.assertTrue(repr(self.family) == repr(persons_family))

    def test_member_in_family(self):
        """This should return True"""
        self.assertTrue("Jay Kim" in self.family)

    def test_person_member_in_family(self):
        """This should return True"""
        self.assertTrue(Person("Jay Kim") in self.family)

    def test_member_not_in_family(self):
        """This should return False"""
        self.assertFalse("Julia" in self.family)

    def test_person_member_not_in_family(self):
        """This should return False"""
        self.assertFalse(Person("Julia") in self.family)

    def test_family_generator(self):
        """The family generator should yield each family members"""
        family_gen = iter(self.family)
        members = []
        for member in family_gen:
            members.append(member)

        expected1 = ["Jay Kim", "Jung Lee"]
        expected2 = ["Jung Lee", "Jay Kim"]
        self.assertTrue(members == expected1 or members == expected2)

    def test_len_family(self):
        """This should return the number of members in the family"""
        self.assertEqual(len(self.family), 2)

    def test_family_eq_with_same_members(self):
        """Families with same members should be the same family"""
        same_family = Family(["Jung Lee", "Jay Kim"])
        self.assertEqual(self.family, same_family)

    def test_persons_family_eq_with_same_members(self):
        """Families with same members should be the same family"""
        same_family = Family([Person("Jung Lee"), Person("Jay Kim")])
        self.assertEqual(self.family, same_family)

    def test_family_eq_with_same_members_in_different_type(self):
        """Families with same members should be the same family"""
        same_members = ["Jay Kim", "Jung Lee"]
        self.assertEqual(self.family, same_members)
        same_members_in_different_order = ["Jung Lee", "Jay Kim"]
        self.assertEqual(self.family, same_members_in_different_order)

    def test_persons_family_eq_with_same_members_in_different_type(self):
        """Families with same members should be the same family"""
        same_members = [Person("Jay Kim"), Person("Jung Lee")]
        self.assertEqual(self.family, same_members)
        same_members_in_different_order = [Person("Jung Lee"), Person("Jay Kim")]
        self.assertEqual(self.family, same_members_in_different_order)

    def test_same_family_members_with_mixed_types(self):
        """Families with mixed types with the same names should be the same family"""
        mixed_members = ["Jay Kim", Person("Jung Lee")]
        mixed_family = Family(mixed_members)
        self.assertEqual(mixed_family, self.family)

    def test_family_not_eq_with_different_members(self):
        """Families with different members should be the different family"""
        different_family = Family(["NEW", "Jay Kim", "Jung Lee"])
        self.assertNotEqual(self.family, different_family)

    def test_persons_family_not_eq_with_different_members(self):
        """Families with different members should be the different family"""
        different_family = Family([Person("NEW"), Person("Jay Kim"), Person("Jung Lee")])
        self.assertNotEqual(self.family, different_family)


class TestDuplicatedFamilyMembers(TestCase):
    """Test ``Family`` with non-unique members"""

    def setUp(self) -> None:
        """Instantiate ``Family`` class with duplicated members"""
        self.family = Family(["Narae Kim", "Jay Kim", "Jung Lee", "Narae Kim"])

    def test_len_family(self):
        """This should return the number of members in the family"""
        self.assertEqual(len(self.family), 3)

    def test_family_eq_with_same_members(self):
        """Families with same members should be the same family"""
        same_family = Family(["Narae Kim", "Jay Kim", "Jung Lee"])
        self.assertEqual(self.family, same_family)

    def test_persons_family_eq_with_same_members(self):
        """Families with same members should be the same family"""
        same_family = Family([Person("Narae Kim"), Person("Jay Kim"), Person("Jung Lee")])
        self.assertEqual(self.family, same_family)

    def test_persons_family_eq_with_same_duplicated_members(self):
        """Families with same members should be the same family"""
        same_duplicated_family = Family(
            [Person("Narae Kim"), Person("Jay Kim"), Person("Jung Lee"), Person("Jung Lee")])
        self.assertEqual(self.family, same_duplicated_family)

    def test_family_not_eq_with_different_members(self):
        """Families with different members should be the different family"""
        different_family = Family(["Thomas", "Hazel", "Derek"])
        self.assertNotEqual(self.family, different_family)

    def test_persons_family_not_eq_with_different_members(self):
        """Families with different members should be the different family"""
        different_family = Family([Person("Thomas"), Person("Hazel"), Person("Derek")])
        self.assertNotEqual(self.family, different_family)


if __name__ == '__main__':
    main()
