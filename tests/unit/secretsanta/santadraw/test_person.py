from unittest import TestCase, main

from secretsanta.santadraw.person import Person


class TestPerson(TestCase):
    """Test ``Person`` with a name"""

    def setUp(self) -> None:
        """Instantiate ``Person`` class with the given name"""
        self.person = Person("Narae Kim")

    def test_repr_method(self):
        """The repr of ``Person`` should guide developers on how to replicate the instance"""
        expected = "Person('Narae Kim')"
        self.assertEqual(repr(self.person), expected)

    def test_str_method(self):
        """The str of ``Person`` will return person's name"""
        expected = "Narae Kim"
        self.assertEqual(str(self.person), expected)

    def test_person_eq_with_same_name_person(self):
        """Test __eq__ with a new Person instance with the same name"""
        self.assertEqual(self.person, Person("Narae Kim"))

    def test_person_eq_with_same_name(self):
        """Test __eq__ with a same name string"""
        self.assertEqual(self.person, "Narae Kim")

    def test_person_hash_with_same_name_person(self):
        """Test __hash__ with a new Person instance with the same name"""
        self.assertEqual(hash(self.person), hash(Person("Narae Kim")))

    def test_person_hash_with_different_person(self):
        """Test __hash__ with a different Person instance"""
        self.assertNotEqual(hash(self.person), hash(Person("DIFFERENT")))

    def test_person_hash_with_same_name(self):
        """
        Test __hash__ with the same name string.
        This may be error-prone as an instance of Person can be overridden with the same name string.
        """
        self.assertEqual(hash(self.person), hash("Narae Kim"))

    def test_person_is_in_last_assignees(self):
        """
        Test if a person is in the ``last_assignees`` queue.
        True if the person was assigned in the last two times. Otherwise, False.

        NOTE: The private attribute ``last_assignees`` should not be modified from outside the function.
        """
        self.assertFalse(self.person.is_person_in_last_assignees(""))

        self.person._last_assignees.append("NEW1")
        self.assertTrue(self.person.is_person_in_last_assignees("NEW1"))

        self.person._last_assignees.append(Person("NEW2"))
        self.assertTrue(self.person.is_person_in_last_assignees("NEW1"))
        self.assertTrue(self.person.is_person_in_last_assignees("NEW2"))

        self.person._last_assignees.append("NEW3")
        self.assertFalse(self.person.is_person_in_last_assignees("NEW1"))
        self.assertTrue(self.person.is_person_in_last_assignees("NEW2"))
        self.assertTrue(self.person.is_person_in_last_assignees("NEW3"))

    def test_update_last_assignees_with(self):
        """Test ``update_last_assignees_with()``"""
        self.person.update_last_assignees_with("NEW1")
        self.assertTrue(self.person.is_person_in_last_assignees("NEW1"))

        self.person.update_last_assignees_with(Person("NEW2"))
        self.assertTrue(self.person.is_person_in_last_assignees("NEW1"))
        self.assertTrue(self.person.is_person_in_last_assignees("NEW2"))

        self.person.update_last_assignees_with(Person("NEW3"))
        self.assertFalse(self.person.is_person_in_last_assignees("NEW1"))
        self.assertTrue(self.person.is_person_in_last_assignees("NEW2"))
        self.assertTrue(self.person.is_person_in_last_assignees("NEW3"))


class TestPersonImmediateFamily(TestCase):
    """Test ``Person`` with a name and immediate family"""

    def test_is_person_in_immediate_family(self):
        """
        Test ``is_person_in_immediate_family()``.
        To make ``_immediate_family`` set for the test, I update the private attribute ``_immediate_family`` directly.
        """
        person = Person("original member")
        person._immediate_family.add("new 1")
        self.assertTrue(person.is_person_in_immediate_family("new 1"))
        self.assertFalse(person.is_person_in_immediate_family("new 2"))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 1")))
        self.assertFalse(person.is_person_in_immediate_family(Person("new 2")))

        person._immediate_family.remove("new 1")
        person._immediate_family.add(Person("new 2"))
        self.assertFalse(person.is_person_in_immediate_family("new 1"))
        self.assertTrue(person.is_person_in_immediate_family("new 2"))
        self.assertFalse(person.is_person_in_immediate_family(Person("new 1")))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 2")))

    def test_init_immediate_family_with_str(self):
        """Instantiate a Person by the argument of ``immediate_family`` in str type"""
        person = Person("original member", ["new 1", "new 2"])
        self.assertTrue(person.is_person_in_immediate_family("new 1"))
        self.assertTrue(person.is_person_in_immediate_family("new 2"))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 1")))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 2")))

    def test_init_immediate_family_with_person(self):
        """Instantiate a Person by the argument of ``immediate_family`` in Person type"""
        person = Person("original member", [Person("new 1"), Person("new 2")])
        self.assertTrue(person.is_person_in_immediate_family("new 1"))
        self.assertTrue(person.is_person_in_immediate_family("new 2"))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 1")))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 2")))

    def test_add_immediate_family_with_str(self):
        """Test ``add_immediate_family_with()`` with a string"""
        person = Person("original member")
        person.add_immediate_family_with("new 1")
        self.assertTrue(person.is_person_in_immediate_family("new 1"))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 1")))
        self.assertFalse(person.is_person_in_immediate_family("new 2"))

        person.add_immediate_family_with("new 2")
        self.assertTrue(person.is_person_in_immediate_family("new 2"))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 1")))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 2")))

    def test_remove_immediate_family_with_str(self):
        """
        Test ``remove_immediate_family_with()`` with a string.
        No error / exception will occur when trying to remove a non-existing person in  ``immediate_family``.
        """
        person = Person("original member", ["new 1", "new 2"])

        person.remove_immediate_family_with("new 1")
        self.assertFalse(person.is_person_in_immediate_family(Person("new 1")))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 2")))

        person.remove_immediate_family_with("new 3")  # no error for non-existing person
        self.assertTrue(person.is_person_in_immediate_family(Person("new 2")))

    def test_add_immediate_family_with_person(self):
        """Test ``add_immediate_family_with()`` with the Person type"""
        person = Person("original member")
        person.add_immediate_family_with(Person("new 1"))
        self.assertTrue(person.is_person_in_immediate_family("new 1"))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 1")))
        self.assertFalse(person.is_person_in_immediate_family("new 2"))

        person.add_immediate_family_with(Person("new 2"))
        self.assertTrue(person.is_person_in_immediate_family("new 2"))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 1")))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 2")))

    def test_remove_immediate_family_with_person(self):
        """
        Test ``remove_immediate_family_with()`` with the Person type.
        No error / exception will occur when trying to remove a non-existing person in  ``immediate_family``.
        """
        person = Person("original member", ["new 1", "new 2"])

        person.remove_immediate_family_with(Person("new 1"))
        self.assertFalse(person.is_person_in_immediate_family(Person("new 1")))
        self.assertTrue(person.is_person_in_immediate_family(Person("new 2")))

        person.remove_immediate_family_with(Person("new 3"))  # no error for non-existing person
        self.assertTrue(person.is_person_in_immediate_family(Person("new 2")))

    def test_get_immediate_family(self):
        """Test ``get_immediate_family()``"""
        immediate_family = {"new 1", "new 2"}
        person = Person("original member", immediate_family)
        self.assertEqual(person.get_immediate_family(), immediate_family)
        self.assertEqual(person.get_immediate_family(), {Person("new 1"), Person("new 2")})


if __name__ == '__main__':
    main()
