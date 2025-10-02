# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    BankingSystem,
    Product,
    ShoppingCart,
    VendingMachine,
    divide,
    get_grade,
    is_even,
    is_triangle,
)

# pylint: disable=missing-function-docstring,unused-import


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


class TestWhiteBoxBankingSystem(unittest.TestCase):
    """
    Unit tests for BankAccount and BankingSystem (exercise 27).
    """

    def setUp(self):
        self.system = BankingSystem()

    def test_authenticate_success(self):
        result = self.system.authenticate("user123", "pass123")
        self.assertTrue(result)
        self.assertIn("user123", self.system.logged_in_users)

    def test_authenticate_failure(self):
        result = self.system.authenticate("user123", "wrongpass")
        self.assertFalse(result)

    def test_authenticate_already_logged_in(self):
        self.system.authenticate("user123", "pass123")
        result = self.system.authenticate("user123", "pass123")
        self.assertFalse(result)  # porque ya estaba logeado

    def test_transfer_without_login(self):
        result = self.system.transfer_money("user123", "receiver", 100, "regular")
        self.assertFalse(result)

    def test_transfer_invalid_type(self):
        self.system.authenticate("user123", "pass123")
        result = self.system.transfer_money("user123", "receiver", 100, "fast")
        self.assertFalse(result)

    def test_transfer_regular_fee_success(self):
        self.system.authenticate("user123", "pass123")
        result = self.system.transfer_money("user123", "receiver", 100, "regular")
        self.assertTrue(result)

    def test_transfer_insufficient_funds(self):
        self.system.authenticate("user123", "pass123")
        result = self.system.transfer_money("user123", "receiver", 2000, "express")
        self.assertFalse(result)


class TestWhiteBoxShoppingCart(unittest.TestCase):
    """
    Unit tests for Product and ShoppingCart (exercise 28).
    """

    def setUp(self):
        self.cart = ShoppingCart()
        self.apple = Product("Apple", 2)
        self.banana = Product("Banana", 3)

    def test_add_product_new_item(self):
        self.cart.add_product(self.apple, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_add_product_existing_item(self):
        self.cart.add_product(self.apple, 1)
        self.cart.add_product(self.apple, 3)
        self.assertEqual(self.cart.items[0]["quantity"], 4)

    def test_remove_product_decrease_quantity(self):
        self.cart.add_product(self.apple, 5)
        self.cart.remove_product(self.apple, 2)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_product_remove_item(self):
        self.cart.add_product(self.apple, 2)
        self.cart.remove_product(self.apple, 2)
        self.assertEqual(len(self.cart.items), 0)

    def test_view_product_output(self):
        msg = self.apple.view_product()
        self.assertEqual(msg, "The product Apple has a price of 2")

    def test_checkout_total(self):
        self.cart.add_product(self.apple, 2)
        self.cart.add_product(self.banana, 3)
        total = sum(
            item["product"].price * item["quantity"] for item in self.cart.items
        )
        self.assertEqual(total, 13)
