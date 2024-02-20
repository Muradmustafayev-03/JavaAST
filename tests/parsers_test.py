import unittest
from src.parsers import *


class TestParsers(unittest.TestCase):
    def test_remove_single_line_comments(self):
        test_cases = {
            # input: expected
            "": "",
            "a": "a",
            "a//": "a",
            "a//\n": "a",
            "a//\nb": "a\nb",
            "a//\n//b": "a",
            "a//\n//b\n": "a",
            "a//\n//b\n//c": "a",
            "a//\n//b\nc": "a\nc",
            "a//\n//b\nc//": "a\nc",
            "a//\n//b\nc//\n": "a\nc",
        }

        for test_input, expected in test_cases.items():
            with self.subTest(input=test_input, expected=expected):
                self.assertEqual(remove_single_line_comments(test_input), expected)

    def test_remove_multi_line_comments(self):
        test_cases = {
            # input: expected
            "": "",
            "a": "a",
            "/* a */ b; c": " b; c",
            "/* a */ b; /* c */ d": " b;  d",
            "a /* b */ c; /* d */ e; /* f */ g": "a  c;  e;  g",
            "a /* b \n b */ c; /* d */ e; /* f */ g": "a  c;  e;  g",
            "a /* b */ c\n; /* d */ e; /* f */ g": "a  c\n;  e;  g",
        }

        for test_input, expected in test_cases.items():
            with self.subTest(input=test_input, expected=expected):
                self.assertEqual(remove_multi_line_comments(test_input), expected)

    def test_parse_package(self):
        test_cases = {
            # input: expected
            "": None,
            "package a;": "a",
            "import package.name.Class;\nimport package.name.*;": None,
            "package a; import package.name.Class;\nimport package.name.*;": "a",
            "// package a;": None,
            "// comment\npackage a;": "a",
            "int a = 0; package a;": None,
        }

        for test_input, expected in test_cases.items():
            with self.subTest(input=test_input, expected=expected):
                self.assertEqual(parse_package(test_input), expected)


if __name__ == '__main__':
    unittest.main()
