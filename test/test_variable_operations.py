import unittest


class TestVariableOperations(unittest.TestCase):
    def test_variables_can_be_added(self):
        an_integer = 3
        a_float = 2.0
        a_string = "abcd"
        a_tuple = (1, 2, 3)
        a_list = [1, 2, 3]
        self.assertEqual(6, an_integer + an_integer)
        self.assertEqual(5, an_integer + 2)
        self.assertEqual(4.0, a_float + a_float)
        self.assertEqual("abcdabcd", a_string + a_string)
        self.assertEqual((1, 2, 3, 1, 2, 3), a_tuple + a_tuple)
        self.assertEqual([1, 2, 3, 1, 2, 3], a_list + a_list)
        self.assertEqual(5.0, an_integer + a_float)

    def test_numerical_variables_can_be_substracted(self):
        an_integer = 3
        a_float = 2.0
        a_string = "abcd"
        a_tuple = (1, 2, 3)
        a_list = [1, 2, 3]
        self.assertEqual(0, an_integer - an_integer)
        self.assertEqual(5, an_integer + 2)
        self.assertEqual(4.0, a_float + a_float)



if __name__ == '__main__':
    unittest.main()
