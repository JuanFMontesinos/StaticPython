import unittest
from staticpython import statictype


class MyBaseClass:
    pass


class MySubClass(MyBaseClass):
    pass


@statictype
def example_function(a: int, b: str) -> None:
    pass


@statictype
def example_function_with_class(param: MyBaseClass) -> None:
    pass


class TestEnforceTypeHints(unittest.TestCase):

    def test_correct_types(self):
        # Should not raise an exception
        try:
            example_function(1, "hello")
        except TypeError:
            self.fail("example_function() raised TypeError unexpectedly!")

    def test_incorrect_positional_argument(self):
        # Should raise an exception
        with self.assertRaises(TypeError):
            example_function("not an int", "hello")

    def test_incorrect_keyword_argument(self):
        # Should raise an exception
        with self.assertRaises(TypeError):
            example_function(1, b=42)

    def test_passing_subclass(self):
        # Should not raise an exception, as MySubClass is a subclass of MyBaseClass
        try:
            example_function_with_class(MySubClass())
        except TypeError:
            self.fail(
                "example_function_with_class() raised TypeError unexpectedly!")


if __name__ == '__main__':
    unittest.main()
