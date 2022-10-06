import unittest


class FirstClass:
    def __init__(self):
        self.a_property = "33"


class AnotherClass:
    def __init__(self):
        self.a_property = 2

    def get_property(self):
        return self.a_property

    @staticmethod
    def a_pure_method(a_parameter):
        return a_parameter * 3


class AClassWithPrivateProperties:
    def __init__(self):
        self.__i_am_private = 43

    def get_secret_of_life(self):
        return self.__i_am_private


class AClassWithInitializationParameters:
    def __init__(self, a_parameter, another_parameter):
        self.a_property = a_parameter
        self.another_property = another_parameter


class TestClasses(unittest.TestCase):
    def test_classes_can_contain_properties(self):
        an_object = AnotherClass()
        self.assertEqual(2, an_object.a_property)

    def test_a_class_can_contain_methods(self):
        a_reference = AnotherClass()
        self.assertEqual(9, a_reference.a_pure_method(3))

    def test_class_initialization_can_be_parameterized(self):
        a_reference = AClassWithInitializationParameters(a_parameter="nice", another_parameter="super_nice")
        self.assertEqual(a_reference.a_property, "nice")
        self.assertEqual(a_reference.another_property, "super_nice")

    def test_methods_that_do_not_depend_on_properties_are_pure_and_should_be_declared_static(self):
        a_reference = AnotherClass()
        self.assertEqual(9, a_reference.a_pure_method(3))

    def test_methods_that_static_can_be_called_without_a_reference(self):
        # Here we're using class as a namespace inside a python module
        self.assertEqual(9, AnotherClass.a_pure_method(3))

    def test_a_method_can_reference_a_property(self):
        a_reference = AnotherClass()
        self.assertEqual(2, a_reference.get_property())

    def test_a_class_property_can_be_changed(self):
        a_reference = AnotherClass()
        a_reference.a_property = 3
        self.assertEqual(3, a_reference.get_property())

    def test_objects_from_the_same_class_are_not_equal(self):
        first_object = AnotherClass()
        second_object = AnotherClass()
        self.assertNotEqual(first_object, second_object)

    def test_objects_from_the_same_class_have_the_same_type(self):
        first_object = AnotherClass()
        second_object = AnotherClass()
        self.assertEqual(first_object.__class__, second_object.__class__)
        self.assertTrue(first_object.__class__ is AnotherClass)
        self.assertTrue(second_object.__class__ is AnotherClass)

    def test_classes_might_have_private_data(self):
        an_object = AClassWithPrivateProperties()
        with self.assertRaises(AttributeError) as e:
            an_object.__i_am_private
        self.assertEqual("'AClassWithPrivateProperties' object has no attribute '_TestClasses__i_am_private'",
                         e.exception.__str__())


if __name__ == '__main__':
    unittest.main()
