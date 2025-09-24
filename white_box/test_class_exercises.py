# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    VendingMachine,
    calculate_total_discount,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_password,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")


class TestWhiteBoxEx1(unittest.TestCase):
    """
    White-box unit tests for the `check_number_status` function.
    This function should return:
      - "Zero" if the number is 0
      - "Positive" if the number is greater than 0
      - "Negative" if the number is less than 0
      - Raise TypeError if the input is not a number
    """

    def test_check_number_status_num_is_zero(self):
        """Should return 'Zero' when the input number is exactly 0."""
        self.assertEqual(check_number_status(0), "Zero")

    def test_check_number_status_num_is_bigger_than_0(self):
        """Should return 'Positive' when the input number is greater than 0."""
        self.assertEqual(check_number_status(1), "Positive")

    def test_check_number_status_num_is_smaller_than_0(self):
        """Should return 'Negative' when the input number is less than 0."""
        self.assertEqual(check_number_status(-1), "Negative")

    def test_check_number_status_with_string(self):
        """Should raise TypeError when the input is not a numeric type."""
        with self.assertRaises(TypeError):
            check_number_status("not_a_number")


class TestWhiteBoxEx2(unittest.TestCase):
    """
    White-box unit tests for the `validate_password` function.
    The password must:
      - Be at least 9 characters long
      - Contain at least one uppercase letter
      - Contain at least one lowercase letter
      - Contain at least one digit
      - Contain at least one special symbol
    """

    def test_validate_password_len_less_than_9(self):
        """Should return False if password length is less than 9 characters."""
        self.assertFalse(validate_password("12345678"))

    def test_validate_password_no_uppercase(self):
        """Should return False if password has no uppercase letters."""
        self.assertFalse(validate_password("abcdefghijk5@"))

    def test_validate_password_no_lowercase(self):
        """Should return False if password has no lowercase letters."""
        self.assertFalse(validate_password("ABCDEFGHIJK5@"))

    def test_validate_password_no_digit(self):
        """Should return False if password has no numeric digits."""
        self.assertFalse(validate_password("ABCDEFGHIJK@"))

    def test_validate_password_no_special_symbol(self):
        """Should return False if password has no special characters."""
        self.assertFalse(validate_password("ABCDEFGHIJK"))


class TestWhiteBoxEx3(unittest.TestCase):
    """
    White-box unit tests for the `calculate_total_discount` function.
    Discount rules:
      - No discount if total is less than 100
      - 10% discount if total is between 100 and 500 (inclusive)
      - 20% discount if total is greater than 500
      - Raise TypeError if the input is not a number
    """

    def test_calculate_total_discount_less_than_100(self):
        """Should return 0 discount when total is less than 100."""
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_more_or_eq_than_100(self):
        """Should return 10% discount when total is exactly 100."""
        self.assertEqual(calculate_total_discount(100), 100 * 0.1)

    def test_calculate_total_discount_less_or_eq_than_500(self):
        """Should return 10% discount when total is exactly 500."""
        self.assertEqual(calculate_total_discount(500), 500 * 0.1)

    def test_calculate_total_discount_more_than_500(self):
        """Should return 20% discount when total is greater than 500."""
        self.assertEqual(calculate_total_discount(501), 501 * 0.2)

    def test_calculate_total_discount_with_string(self):
        """Should raise TypeError when the input is not a numeric type."""
        with self.assertRaises(TypeError):
            check_number_status("not_a_number")