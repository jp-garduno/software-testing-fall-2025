# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
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


class TestWhiteBoxCheckNumberStatus(unittest.TestCase):
    """
    Check Number Status unit tests.
    """

    def test_check_number_status_positive(self):
        """
        Checks if a positive number is correctly identified.
        """
        self.assertEqual(check_number_status(5), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks if a negative number is correctly identified.
        """
        self.assertEqual(check_number_status(-3), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks if zero is correctly identified.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_check_number_status_positive_decimal(self):
        """
        Checks if a positive decimal number is correctly identified.
        """
        self.assertEqual(check_number_status(2.5), "Positive")

    def test_check_number_status_negative_decimal(self):
        """
        Checks if a negative decimal number is correctly identified.
        """
        self.assertEqual(check_number_status(-1.7), "Negative")

    def test_check_number_status_positive_large_number(self):
        """
        Checks if a large positive number is correctly identified.
        """
        self.assertEqual(check_number_status(float("inf")), "Positive")

    def test_check_number_status_negative_large_number(self):
        """
        Checks if a large negative number is correctly identified.
        """
        self.assertEqual(check_number_status(-float("inf")), "Negative")


class TestValidatePassword(unittest.TestCase):
    """
    Validate Password unit tests.
    """

    def test_password_length_less_than_8(self):
        """
        Checks if a password's length is less than 8
        """
        self.assertEqual(validate_password("1234#Ab"), False)

    def test_password_length_equal_to_8(self):
        """
        Checks if a password's length is equal to 8
        """
        self.assertEqual(validate_password("1234#Abc"), True)

    def test_password_length_more_than_8(self):
        """
        Checks if a password's length is more than 8
        """
        self.assertEqual(validate_password("1234#Abcd"), True)

    def test_password_missing_uppercase(self):
        """
        Checks if a password without uppercase letter is invalid
        """
        self.assertEqual(validate_password("1234#abc"), False)

    def test_password_missing_lowercase(self):
        """
        Checks if a password without lowercase letter is invalid
        """
        self.assertEqual(validate_password("1234#ABC"), False)

    def test_password_missing_digit(self):
        """
        Checks if a password without digit is invalid
        """
        self.assertEqual(validate_password("abcd#Abc"), False)

    def test_password_missing_special_char(self):
        """
        Checks if a password without special character is invalid
        """
        self.assertEqual(validate_password("1234Abcd"), False)


class TestCalculateTotalDiscount(unittest.TestCase):
    """
    Calculate Total Discount unit tests.
    """

    def test_total_amount_less_than_100(self):
        """
        Checks if no discount is applied when total amount is less than 100.
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_total_amount_less_than_100_frontier(self):
        """
        Checks if no discount is applied when total amount is 99 (boundary value).
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_total_amount_equals_100(self):
        """
        Checks if 10% discount is applied when total amount equals 100.
        """
        self.assertEqual(calculate_total_discount(100), 0.1 * 100)

    def test_total_amount_more_than_100(self):
        """
        Checks if 10% discount is applied when total amount is between 100 and 500.
        """
        self.assertEqual(calculate_total_discount(300), 0.1 * 300)

    def test_total_amount_equals_500(self):
        """
        Checks if 10% discount is applied when total amount equals 500.
        """
        self.assertEqual(calculate_total_discount(500), 0.1 * 500)

    def test_total_amount_more_than_500_frontier(self):
        """
        Checks if 20% discount is applied when total amount is 501 (boundary value).
        """
        self.assertEqual(calculate_total_discount(501), 0.2 * 501)

    def test_total_amount_more_than_500(self):
        """
        Checks if 20% discount is applied when total amount is greater than 500.
        """
        self.assertEqual(calculate_total_discount(600), 0.2 * 600)


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


class TestTrafficLight(unittest.TestCase):
    """
    Traffic Light unit tests.
    """

    def setUp(self):
        """
        Set up a new TrafficLight instance for each test.
        """
        self.traffic_light = TrafficLight()

    def test_get_state(self):
        """
        Checks if the get_current_state function works correctly.
        """
        state = self.traffic_light.get_current_state()
        self.assertEqual(state, "Red")

    def test_change_from_red(self):
        """
        Checks if the state changes from red to green correctly.
        """
        self.traffic_light.change_state()
        state = self.traffic_light.get_current_state()
        self.assertEqual(state, "Green")

    def test_change_from_green(self):
        """
        Checks if the state changes from green to yellow correctly.
        """
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()
        state = self.traffic_light.get_current_state()
        self.assertEqual(state, "Yellow")

    def test_change_from_yellow(self):
        """
        Checks if the state changes from yellow to red correctly.
        """
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()
        state = self.traffic_light.get_current_state()
        self.assertEqual(state, "Red")
