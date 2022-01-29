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
        """Test __eq__ a same name string"""
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

    def test_person_is_in_last_queue(self):
        """
        Test if a person is in the ``last_assignees`` queue.
        True if the person was assigned in the last two times. Otherwise, False.

        NOTE: The private attribute ``_last_queue`` should not be modified from outside the function.
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

    def test_update_last_queue_with(self):
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


if __name__ == '__main__':
    main()
