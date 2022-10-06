import unittest

_hidden_state = 0


class TestFunctions(unittest.TestCase):
    def test_a_function_can_be_declared_empty(self):
        def a_nice_function():
            pass

        self.assertEqual(None, a_nice_function())  # add assertion here

    def test_a_function_can_return_something(self):
        def a_nicer_function():
            return 42

        self.assertEqual(42, a_nicer_function())

    def test_a_function_can_even_return_more_than_one_thing_using_a_tuple(self):
        def a_function_that_returns_more_than_one_thing():
            return (4, 3)  # return 4,4 would be more pythonic, but less explicit

        self.assertEqual((4, 3), a_function_that_returns_more_than_one_thing())

    def test_a_function_can_receive_parameters(self):
        def a_parameter_receiving_function(a_parameter):
            return a_parameter * 3

        self.assertEqual(9, a_parameter_receiving_function(3))

    def test_a_parameter_can_be_positional(self):
        def a_function(a_parameter, another_parameter):
            return another_parameter

        self.assertEqual(4, a_function(1, 3))

    def test_a_parameter_can_be_specified_using_its_name(self):
        def a_function(a_parameter, another_parameter):
            return another_parameter

        self.assertEqual(3, a_function(another_parameter=3, a_parameter=1))

    def test_a_parameter_can_have_a_default_value(self):
        def a_function(a_parameter=3):
            return a_parameter

        self.assertEqual(3, a_function())

    def test_a_function_can_fail_by_rising_an_exception(self):
        def a_function_that_that_fails_hard():
            raise RuntimeError("Something very bad happened")

        with self.assertRaises(RuntimeError) as e:
            a_function_that_that_fails_hard()

        self.assertEqual("Something very bad happened", e.exception.__str__())

    def test_pure_functions_depend_only_on_given_parameters(self):
        def a_pure_function(a_parameter):
            return a_parameter * 2

        self.assertEqual(4, a_pure_function(2))
        self.assertEqual(4, a_pure_function(2))
        self.assertEqual(4, a_pure_function(2))

    def test_an_impure_function_depends_on_something_else_beyond_parameters(self):
        def an_impure_function(a_parameter):
            global _hidden_state
            _hidden_state += 1
            return a_parameter * 2 + _hidden_state

        self.assertEqual(5, an_impure_function(2))
        self.assertEqual(6, an_impure_function(2))


if __name__ == '__main__':
    unittest.main()
