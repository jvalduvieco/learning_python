import unittest
from dataclasses import dataclass, field, FrozenInstanceError, replace
from typing import List


@dataclass()
class Car:
    plate: str
    serial_number: str
    build_year: int


@dataclass(frozen=True)
class StonePlate:
    text: str


class TestDataClasses(unittest.TestCase):
    def test_a_dataclass_can_be_created(self):
        self.assertTrue(Car(plate="6666XXX", serial_number="Q239881991", build_year=2015))

    def test_dataclasses_are_equal_if_properties_are_equal(self):
        a_nice_car = Car(plate="14MC00L", serial_number="Q239881991", build_year=2022)
        same_car = Car(plate="14MC00L", serial_number="Q239881991", build_year=2022)
        self.assertEqual(a_nice_car, same_car)
        a_nice_car.plate = "14MN07C00L"
        self.assertNotEqual(a_nice_car, same_car)

    def test_properties_can_have_default_values(self):
        @dataclass()
        class WeirdClass:
            an_integer: int = field(default=3)
            a_list: List[int] = field(default_factory=list)
            a_boolean: bool = field(default=True)

        self.assertEqual(3, WeirdClass().an_integer)

    def test_dataclasses_can_be_immutable(self):
        tombstone = StonePlate(text="Here lies John Doe")
        with self.assertRaises(FrozenInstanceError):
            tombstone.text = "Here lies John Doe Jr"

    def test_immutable_dataclasses_can_be_copied_to_a_new_class_and_modified(self):
        tombstone = StonePlate(text="Here lies John Doe")
        neighbour_tombstone = replace(tombstone, text="Here lies John Doe's neighbour")

        self.assertNotEqual(tombstone, neighbour_tombstone)
        self.assertEqual("Here lies John Doe's neighbour", neighbour_tombstone.text)


if __name__ == '__main__':
    unittest.main()
