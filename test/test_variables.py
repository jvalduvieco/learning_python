import unittest


class AClass:
    def __init__(self):
        self.a_property = "abcd"


class TestVariables(unittest.TestCase):
    def test_variables_can_hold_booleans(self):
        a_boolean = True
        another_boolean = False
        self.assertEqual(True, a_boolean)
        self.assertTrue(a_boolean)
        self.assertEqual(False, another_boolean)
        self.assertFalse(another_boolean)

    def test_variables_can_hold_integers(self):
        a_integer = 3
        self.assertEqual(3, a_integer)

    def test_variables_can_hold_floats(self):
        a_float = 0.3
        self.assertEqual(0.3, a_float)

    def test_variables_can_hold_strings(self):
        a_string = "aaaa"
        self.assertEqual("aaaa", a_string)

    def test_variables_can_hold_lists(self):
        a_list = [1, 2, 3]
        self.assertEqual([1, 2, 3], a_list)

    def test_variables_can_hold_tuples(self):
        a_tuple = (2, 3)
        self.assertEqual((2, 3), a_tuple)

    def test_variables_can_hold_complex_data_types(self):
        # A reference is the memory direction of a complex data type
        a_reference = AClass()
        self.assertNotEqual(AClass(), a_reference)
        self.assertEqual("abcd", a_reference.a_property)

    def test_variables_can_hold_functions(self):
        a_function = lambda x: x + 3
        self.assertEqual(6, a_function(3))


if __name__ == '__main__':
    unittest.main()
