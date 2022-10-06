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

    def test_boolean_variables_can_be_combined_using_logical_operators(self):
        i_am_true = True
        i_am_false = False
        self.assertTrue(i_am_true and i_am_true)
        self.assertFalse(i_am_false and i_am_false)
        self.assertFalse(i_am_true and i_am_false)
        self.assertTrue(i_am_true and not i_am_false)
        self.assertTrue(not i_am_false and not i_am_false)
        self.assertTrue(i_am_true or i_am_false)
        self.assertFalse(i_am_false or i_am_false)
        self.assertTrue(i_am_false or not i_am_false)
        self.assertTrue(i_am_true is True)
        self.assertTrue(i_am_false is False)


if __name__ == '__main__':
    unittest.main()
