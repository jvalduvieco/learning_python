import abc
import unittest
from abc import ABC


class Parent:
    def __init__(self):
        self.a_nice_parent_property = 32
        self._a_family_secret_property = 13

    def a_nice_parent_method(self):
        return self.a_nice_parent_property * 3


class AnotherParent:
    @staticmethod
    def another_parent_method():
        return 3


class Child(Parent):
    def __init__(self):
        super().__init__()

    def reveal_family_secret(self):
        return self._a_family_secret_property


class AChildWithMultipleParents(Parent, AnotherParent):
    pass


class AContractClass(ABC):
    @abc.abstractmethod
    def should_do_this(self):
        pass

    @abc.abstractmethod
    def should_do_that(self):
        pass


class ClassInheritance(unittest.TestCase):
    def test_a_class_can_inherit_properties_from_a_parent_class(self):
        an_object = Child()
        self.assertEqual(32, an_object.a_nice_parent_property)

    def test_a_class_can_inherit_methods_from_a_parent_class(self):
        an_object = Child()
        self.assertEqual(96, an_object.a_nice_parent_method())

    def test_a_class_can_have_properties_only_visible_to_their_children_and_clients_who_know_too_much(self):
        an_object = Child()
        self.assertEqual(13, an_object.reveal_family_secret())
        # an_object._a_family_secret_property won't appear in your ide but is accessible
        self.assertEqual(13, an_object._a_family_secret_property)

    def test_class_ancestors_can_be_checked(self):
        an_object = Child()
        self.assertTrue(Parent in an_object.__class__.__mro__)

    def test_multiple_class_ancestors_can_be_checked(self):
        an_object = AChildWithMultipleParents()
        self.assertTrue(Parent in an_object.__class__.__mro__)
        self.assertTrue(AnotherParent in an_object.__class__.__mro__)

    def test_contract_classes_can_not_be_instantiated(self):
        # Others name these classes "Abstract" as they have no implementation, just define an interface (contract)
        # to its clients
        with self.assertRaises(TypeError) as e:
            AContractClass()

        self.assertEqual(
            "Can't instantiate abstract class AContractClass with abstract methods class_should_do_that, class_should_do_this",
            e.exception.__str__())

    def test_contract_classes_must_be_implemented_by_another_class(self):
        class AContractImplementation(AContractClass):
            def should_do_this(self):
                return 1

            def should_do_that(self):
                return 2

        an_object = AContractImplementation()
        self.assertEqual(1, an_object.should_do_this())

    def test_contract_classes_can_be_implemented_by_several_classes(self):
        class AContractImplementation(AContractClass):
            def should_do_this(self):
                return 1

            def should_do_that(self):
                return 2

        class AnotherContractImplementation(AContractClass):
            def should_do_this(self):
                return 3 - 2

            def should_do_that(self):
                return 1 * 2

        an_object = AContractImplementation()
        another_object = AnotherContractImplementation()

        self.assertEqual(1, an_object.should_do_this())
        self.assertEqual(1, another_object.should_do_this())


if __name__ == '__main__':
    unittest.main()
