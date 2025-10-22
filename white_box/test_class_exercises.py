# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_email,
    validate_login,
    validate_password,
    verify_age,
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


class TestCheckNumberStatus(unittest.TestCase):
    """
    Check number status unit tests.
    """

    def test_check_number_status_negative(self):
        """
        Checks negative number.
        """
        self.assertEqual(check_number_status(-5), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_check_number_status_positive_even(self):
        """
        Checks positive even number.
        """
        self.assertEqual(check_number_status(8), "Positive")

    def test_check_number_status_positive_odd(self):
        """
        Checks positive odd number.
        """
        self.assertEqual(check_number_status(7), "Positive")


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
    Validate password unit tests.
    """

    def test_validate_password_too_short(self):
        """
        Checks password length.
        """
        self.assertFalse(validate_password("short"))

    def test_validate_password_no_number(self):
        """
        Checks password for numbers.
        """
        self.assertFalse(validate_password("NoNumber"))

    def test_validate_password_no_uppercase(self):
        """
        Checks password for uppercase letters.
        """
        self.assertFalse(validate_password("nouppercase1"))

    def test_validate_password_no_special_characters(self):
        """
        Checks password for special characters.
        """
        self.assertFalse(validate_password("NoSpecial1"))

    def test_validate_password_valid(self):
        """
        Checks valid password.
        """
        self.assertTrue(validate_password("Valid1Password!"))

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
        Tests no uppercase
        """
        self.assertEqual(validate_password("1234#abc"), False)

    def test_password_missing_lowercase(self):
        """
        tests no lowercase
        """
        self.assertEqual(validate_password("1234#ABC"), False)

    def test_password_missing_digit(self):
        """
        Tests no digits
        """
        self.assertEqual(validate_password("abcd#Abc"), False)

    def test_password_missing_special_char(self):
        """
        Tests no special char
        """
        self.assertEqual(validate_password("1234Abcd"), False)


class TestCalculateTotalDiscount(unittest.TestCase):
    """
    Calculate total discount unit tests.
    """

    def test_calculate_total_discount_no_discount(self):
        """
        Checks no discount applied.
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_10_percent_lower_limit(self):
        """
        Checks 10 percent discount applied for lower limit.
        """
        self.assertEqual(calculate_total_discount(100), 10)

    def test_calculate_total_discount_10_percent_upper_limit(self):
        """
        Checks 10 percent discount applied for upper limit.
        """
        self.assertEqual(calculate_total_discount(500), 50)

    def test_calculate_total_discount_20_percent(self):
        """
        Checks 20 percent discount applied.
        """
        self.assertEqual(calculate_total_discount(501), 0.2 * 501)

    def test_total_amount_less_than_100(self):
        """
        Checks if no discount is applied when total amount is less than 100.
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_total_amount_less_than_100_frontier(self):
        """
        Tests exactly 99
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_total_amount_equals_100(self):
        """
        Tests exactly 100
        """
        self.assertEqual(calculate_total_discount(100), 0.1 * 100)

    def test_total_amount_more_than_100(self):
        """
        Tests between 100 and 500
        """
        self.assertEqual(calculate_total_discount(300), 0.1 * 300)

    def test_total_amount_equals_500(self):
        """
        Tests amount exactly 500
        """
        self.assertEqual(calculate_total_discount(500), 0.1 * 500)

    def test_total_amount_more_than_500_frontier(self):
        """
        Tests exactly 501
        """
        self.assertEqual(calculate_total_discount(501), 0.2 * 501)


class TestCalculateOrderTotal(unittest.TestCase):
    """
    Calculate Order Total unit tests
    """

    def test_empty_order(self):
        """
        Tests that an empty order returns zero total
        """
        items = []
        self.assertEqual(calculate_order_total(items), 0)

    def test_single_item_no_discount(self):
        """
        Tests a single item with quantity in the no-discount range
        """
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_single_item_small_discount(self):
        """
        Tests a single item with quantity in the 5% discount range
        """
        items = [{"quantity": 8, "price": 10}]
        self.assertEqual(calculate_order_total(items), 76)

    def test_single_item_large_discount(self):
        """
        Tests a single item with quantity in the 10% discount range
        """
        items = [{"quantity": 15, "price": 10}]
        self.assertEqual(calculate_order_total(items), 135)

    def test_multiple_items_mixed_discounts(self):
        """
        Tests multiple items with different quantities that fall into different discount ranges
        """
        items = [
            {"quantity": 3, "price": 10},
            {"quantity": 8, "price": 20},
            {"quantity": 12, "price": 5},
        ]
        self.assertEqual(calculate_order_total(items), 236)

    def test_boundary_values_lower(self):
        """
        Tests boundary values at the lower end of each discount range
        """
        items = [
            {"quantity": 1, "price": 10},
            {"quantity": 6, "price": 10},
            {"quantity": 11, "price": 10},
        ]
        self.assertEqual(calculate_order_total(items), 166)

    def test_boundary_values_upper(self):
        """
        Tests boundary values at the upper end of each discount range
        """
        items = [
            {"quantity": 5, "price": 10},
            {"quantity": 10, "price": 10},
        ]
        self.assertEqual(calculate_order_total(items), 145)

    def test_zero_quantity(self):
        """
        Tests that items with zero quantity don't affect the total
        """
        items = [{"quantity": 0, "price": 10}, {"quantity": 3, "price": 5}]
        self.assertEqual(calculate_order_total(items), 15)

    def test_negative_quantity(self):
        """
        Tests negative quantities
        """
        items = [{"quantity": -2, "price": 10}]
        self.assertEqual(calculate_order_total(items), -18)

    def test_large_values(self):
        """
        Tests overflow
        """
        items = [{"quantity": 1000000, "price": 1000}]
        self.assertEqual(calculate_order_total(items), 900000000)


class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    Calculate Items Shipping Cost unit tests.
    """

    def test_empty_order_standard(self):
        """
        Tests shipping cost for an empty order with standard shipping
        """
        items = []
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_empty_order_express(self):
        """
        Tests shipping cost for an empty order with express shipping
        """
        items = []
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_standard_shipping_light_items(self):
        """
        Tests standard shipping for items with total weight <= 5
        """
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_medium_items(self):
        """
        Tests standard shipping for items with total weight between 5 and 10
        """
        items = [{"weight": 3}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_heavy_items(self):
        """
        Tests standard shipping for items with total weight > 10
        """
        items = [{"weight": 5}, {"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_express_shipping_light_items(self):
        """
        Tests express shipping for items with total weight <= 5
        """
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_medium_items(self):
        """
        Tests weight between 5 and 10 express
        """
        items = [{"weight": 3}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_shipping_heavy_items(self):
        """
        Tests weight > 10 express
        """
        items = [{"weight": 5}, {"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_boundary_weight_standard_low(self):
        """
        Tests weight exactly 5 standard
        """
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_boundary_weight_standard_high(self):
        """
        Tests weight exactly 10 standard
        """
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_boundary_weight_express_low(self):
        """
        Tests weight exactly 5 express
        """
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_boundary_weight_express_high(self):
        """
        Tests weigth exactly 10 express
        """
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_decimal_weight(self):
        """
        Tests shipping with decimal weights
        """
        items = [{"weight": 2.5}, {"weight": 2.5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_invalid_shipping_method(self):
        """
        Tests invalid shipping method raises a ValueError.
        """
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "priority")

    def test_negative_weights(self):
        """
        Tests negative weights
        """
        items = [{"weight": -3}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_large_weights(self):
        """
        Tests with very large weights.
        """
        items = [{"weight": 1000000}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)


class TestValidateLogin(unittest.TestCase):
    """
    White box tests for validate_login function
    """

    def test_correct_username_correct_password(self):
        """
        Tests valid username and password
        """
        self.assertEqual(validate_login("samupif", "123456789"), "Login Successful")

    def test_username_correct_password_less_than_8(self):
        """
        Tests correct username and password length less than 8
        """
        self.assertEqual(validate_login("samupif", "12345"), "Login Failed")

    def test_username_correct_password_more_than_15(self):
        """
        Tests correct username and password length more than 15
        """
        self.assertEqual(
            validate_login("samupif", "123456789abcdefghi"), "Login Failed"
        )

    def test_username_less_than_5_password_correct(self):
        """
        Tests username length less than 5 with valid password
        """
        self.assertEqual(validate_login("samu", "123456789"), "Login Failed")

    def test_username_more_than_20_password_correct(self):
        """
        Tests username length more than 20 with valid password
        """
        self.assertEqual(
            validate_login("samuelpiafigueroa123456789", "123456789"), "Login Failed"
        )

    def test_username_exactly_5_password_correct(self):
        """
        Tests username length exactly 5 with valid password
        """
        self.assertEqual(validate_login("samue", "123456789"), "Login Successful")

    def test_username_exactly_20_password_correct(self):
        """
        Tests username length exactly 20 with valid password
        """
        self.assertEqual(
            validate_login("samuesamuesamuesamue", "123456789"), "Login Successful"
        )

    def test_username_correct_password_exactly_8(self):
        """
        Tests correct username and password length exactly 8
        """
        self.assertEqual(validate_login("samupif", "12345678"), "Login Successful")

    def test_username_correct_password_exactly_15(self):
        """
        Tests correct username and password length exactly 15
        """
        self.assertEqual(
            validate_login("samupif", "123456789abcdfg"), "Login Successful"
        )


class TestVerifyAge(unittest.TestCase):
    """
    White box tests for verify_age function
    """

    def test_valid_age(self):
        """
        Tests a valid age between the range
        """
        self.assertEqual(verify_age(20), "Eligible")

    def test_age_less_than_18(self):
        """
        Test age outside range in the lower end
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_age_more_than_65(self):
        """
        Test age outside range in the upper end
        """
        self.assertEqual(verify_age(66), "Not Eligible")

    def test_age_exactly_18(self):
        """
        Test age exactly 18
        """
        self.assertEqual(verify_age(18), "Eligible")

    def test_age_exactly_65(self):
        """
        Test age exactly 65
        """
        self.assertEqual(verify_age(65), "Eligible")


class TestCategorizeProduct(unittest.TestCase):
    """
    White box tests categorize_product function
    """

    def test_price_category_d_less_than_10(self):
        """
        Tests price less than 10
        """
        self.assertEqual(categorize_product(5), "Category D")

    def test_price_category_a(self):
        """
        Tests price between 10 and 50
        """
        self.assertEqual(categorize_product(15), "Category A")

    def test_price_category_a_exactly_bottom(self):
        """
        Tests price exactly 10
        """
        self.assertEqual(categorize_product(10), "Category A")

    def test_price_category_a_exactly_upper(self):
        """
        Tests price exactly 50
        """
        self.assertEqual(categorize_product(50), "Category A")

    def test_price_category_b(self):
        """
        Tests price between 51 and 100
        """
        self.assertEqual(categorize_product(75), "Category B")

    def test_price_category_b_exactly_bottom(self):
        """
        Tests price exactly 10
        """
        self.assertEqual(categorize_product(51), "Category B")

    def test_price_category_b_exactly_upper(self):
        """
        Tests price exactly 100
        """
        self.assertEqual(categorize_product(100), "Category B")

    def test_price_category_c(self):
        """
        Tests price between 101 and 200
        """
        self.assertEqual(categorize_product(150), "Category C")

    def test_price_category_c_exactly_bottom(self):
        """
        Tests price exactly 101
        """
        self.assertEqual(categorize_product(101), "Category C")

    def test_price_category_c_exactly_upper(self):
        """
        Tests price exactly 200
        """
        self.assertEqual(categorize_product(200), "Category C")

    def test_price_category_d(self):
        """
        Tests price more than 200
        """
        self.assertEqual(categorize_product(250), "Category D")


class TestValidateEmail(unittest.TestCase):
    """
    White box tests for validate_email function
    """

    def test_valid_email(self):
        """
        Tests a valid email
        """
        email = "user@example.com"
        self.assertEqual(validate_email(email), "Valid Email")

    def test_email_too_short(self):
        """
        Tests an email less than 5 characters
        """
        email = "a@b."
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_email_exactly_min_length(self):
        """
        Tests email exactly 5 characters
        """
        email = "a@b.c"
        self.assertEqual(validate_email(email), "Valid Email")

    def test_email_exactly_max_length(self):
        """
        Tests email exactly 50 characters
        """
        email = "a" * 46 + "@b.c"
        self.assertEqual(validate_email(email), "Valid Email")

    def test_email_too_long(self):
        """
        Tests email more than 50 characters
        """
        email = "a" * 47 + "@b.c"
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_email_missing_at_symbol(self):
        """
        Tests email without the @ symbol
        """
        email = "userexample.com"
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_email_missing_dot(self):
        """
        Tests email without the dot
        """
        email = "user@examplecom"
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_empty_email(self):
        """
        Tests empty email
        """
        email = ""
        self.assertEqual(validate_email(email), "Invalid Email")


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    White box tests for celsius_to_fahrenheit function
    """

    def test_zero_celsius(self):
        """
        Tests 0 C
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_positive_celsius(self):
        """
        Tests positive C value
        """
        self.assertEqual(celsius_to_fahrenheit(25), 77)

    def test_negative_celsius(self):
        """
        Tests negative C value
        """
        self.assertEqual(celsius_to_fahrenheit(-15), 5)

    def test_fractional_celsius(self):
        """
        Tests decimal C value
        """
        self.assertAlmostEqual(celsius_to_fahrenheit(37.5), 99.5)

    def test_lower_boundary(self):
        """
        Tests exactly -100C
        """
        self.assertEqual(celsius_to_fahrenheit(-100), -148)

    def test_upper_boundary(self):
        """
        Tests exactly 100C
        """
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_below_lower_boundary(self):
        """
        Tests less than -100
        """
        self.assertEqual(celsius_to_fahrenheit(-100.1), "Invalid Temperature")

    def test_above_upper_boundary(self):
        """
        Tests more than 100C
        """
        self.assertEqual(celsius_to_fahrenheit(100.1), "Invalid Temperature")


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
