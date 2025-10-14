# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    calculate_quantity_discount,
    calculate_shipping_cost,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    validate_credit_card,
    validate_date,
    validate_url,
)


class TestValidateEmail(unittest.TestCase):
    """
    test cases for validate email function
    """

    def test_validate_credit_card_valid_13_digits(self):
        """
        Checks a valid credit card with 13 digits.
        """
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_valid_14_digits(self):
        """
        Checks a valid credit card with 14 digits.
        """
        self.assertEqual(validate_credit_card("12345678901234"), "Valid Card")

    def test_validate_credit_card_valid_15_digits(self):
        """
        Checks a valid credit card with 15 digits.
        """
        self.assertEqual(validate_credit_card("123456789012345"), "Valid Card")

    def test_validate_credit_card_valid_16_digits(self):
        """
        Checks a valid credit card with 16 digits.
        """
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_validate_credit_card_invalid_too_short(self):
        """
        Checks an invalid credit card with less than 13 digits.
        """
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_invalid_too_long(self):
        """
        Checks an invalid credit card with more than 16 digits.
        """
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_invalid_contains_letters(self):
        """
        Checks an invalid credit card containing letters.
        """
        self.assertEqual(validate_credit_card("123456789012A"), "Invalid Card")

    def test_validate_credit_card_invalid_contains_special_chars(self):
        """
        Checks an invalid credit card containing special characters.
        """
        self.assertEqual(validate_credit_card("1234-5678-9012-3456"), "Invalid Card")

    def test_validate_credit_card_invalid_empty_string(self):
        """
        Checks an invalid credit card with empty string.
        """
        self.assertEqual(validate_credit_card(""), "Invalid Card")

    def test_validate_credit_card_invalid_spaces(self):
        """
        Checks an invalid credit card containing spaces.
        """
        self.assertEqual(validate_credit_card("1234 5678 9012 3456"), "Invalid Card")


class TestValidateDate(unittest.TestCase):
    """
    test cases for validate date function
    """

    def test_validate_date_valid_middle_values(self):
        """
        Checks a valid date with middle range values.
        """
        self.assertEqual(validate_date(2000, 6, 15), "Valid Date")

    def test_validate_date_valid_min_year(self):
        """
        Checks a valid date with minimum year.
        """
        self.assertEqual(validate_date(1900, 6, 15), "Valid Date")

    def test_validate_date_valid_max_year(self):
        """
        Checks a valid date with maximum year.
        """
        self.assertEqual(validate_date(2100, 6, 15), "Valid Date")

    def test_validate_date_valid_min_month(self):
        """
        Checks a valid date with minimum month.
        """
        self.assertEqual(validate_date(2000, 1, 15), "Valid Date")

    def test_validate_date_valid_max_month(self):
        """
        Checks a valid date with maximum month.
        """
        self.assertEqual(validate_date(2000, 12, 15), "Valid Date")

    def test_validate_date_valid_min_day(self):
        """
        Checks a valid date with minimum day.
        """
        self.assertEqual(validate_date(2000, 6, 1), "Valid Date")

    def test_validate_date_valid_max_day(self):
        """
        Checks a valid date with maximum day.
        """
        self.assertEqual(validate_date(2000, 6, 31), "Valid Date")

    def test_validate_date_invalid_year_too_low(self):
        """
        Checks an invalid date with year below 1900.
        """
        self.assertEqual(validate_date(1899, 6, 15), "Invalid Date")

    def test_validate_date_invalid_year_too_high(self):
        """
        Checks an invalid date with year above 2100.
        """
        self.assertEqual(validate_date(2101, 6, 15), "Invalid Date")

    def test_validate_date_invalid_month_zero(self):
        """
        Checks an invalid date with month equal to 0.
        """
        self.assertEqual(validate_date(2000, 0, 15), "Invalid Date")

    def test_validate_date_invalid_month_too_high(self):
        """
        Checks an invalid date with month above 12.
        """
        self.assertEqual(validate_date(2000, 13, 15), "Invalid Date")

    def test_validate_date_invalid_day_zero(self):
        """
        Checks an invalid date with day equal to 0.
        """
        self.assertEqual(validate_date(2000, 6, 0), "Invalid Date")

    def test_validate_date_invalid_day_too_high(self):
        """
        Checks an invalid date with day above 31.
        """
        self.assertEqual(validate_date(2000, 6, 32), "Invalid Date")

    def test_validate_date_invalid_all_parameters_low(self):
        """
        Checks an invalid date with all parameters below their minimum.
        """
        self.assertEqual(validate_date(1800, 0, 0), "Invalid Date")

    def test_validate_date_invalid_all_parameters_high(self):
        """
        Checks an invalid date with all parameters above their maximum.
        """
        self.assertEqual(validate_date(2200, 13, 32), "Invalid Date")

    def test_validate_date_valid_boundary_combination(self):
        """
        Checks a valid date with all minimum boundary values.
        """
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")

    def test_validate_date_valid_max_boundary_combination(self):
        """
        Checks a valid date with all maximum boundary values.
        """
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")


class TestCheckFlightEligibility(unittest.TestCase):
    """
    test cases for check flight eligibility function
    """

    def test_check_flight_eligibility_valid_age_not_frequent(self):
        """
        Checks eligibility with valid age and not frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_check_flight_eligibility_min_age_not_frequent(self):
        """
        Checks eligibility with minimum age and not frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_check_flight_eligibility_max_age_not_frequent(self):
        """
        Checks eligibility with maximum age and not frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_check_flight_eligibility_valid_age_frequent(self):
        """
        Checks eligibility with valid age and frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(30, True), "Eligible to Book")

    def test_check_flight_eligibility_below_min_age_not_frequent(self):
        """
        Checks ineligibility with age below 18 and not frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_check_flight_eligibility_above_max_age_not_frequent(self):
        """
        Checks ineligibility with age above 65 and not frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")

    def test_check_flight_eligibility_below_min_age_frequent(self):
        """
        Checks eligibility with age below 18 but frequent flyer (overrides age restriction).
        """
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")

    def test_check_flight_eligibility_above_max_age_frequent(self):
        """
        Checks eligibility with age above 65 but frequent flyer (overrides age restriction).
        """
        self.assertEqual(check_flight_eligibility(66, True), "Eligible to Book")

    def test_check_flight_eligibility_child_not_frequent(self):
        """
        Checks ineligibility with child age and not frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(10, False), "Not Eligible to Book")

    def test_check_flight_eligibility_senior_not_frequent(self):
        """
        Checks ineligibility with senior age and not frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(80, False), "Not Eligible to Book")

    def test_check_flight_eligibility_child_frequent(self):
        """
        Checks eligibility with child age but frequent flyer status.
        """
        self.assertEqual(check_flight_eligibility(10, True), "Eligible to Book")

    def test_check_flight_eligibility_senior_frequent(self):
        """
        Checks eligibility with senior age but frequent flyer status.
        """
        self.assertEqual(check_flight_eligibility(80, True), "Eligible to Book")

    def test_check_flight_eligibility_min_age_frequent(self):
        """
        Checks eligibility with minimum age and frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(18, True), "Eligible to Book")

    def test_check_flight_eligibility_max_age_frequent(self):
        """
        Checks eligibility with maximum age and frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(65, True), "Eligible to Book")


class TestValidateUrl(unittest.TestCase):
    """
    test cases for validate url function
    """

    def test_validate_url_valid_http_short(self):
        """
        Checks a valid URL with http protocol and short length.
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_valid_https_short(self):
        """
        Checks a valid URL with https protocol and short length.
        """
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_valid_http_max_length(self):
        """
        Checks a valid URL with http protocol and exactly 255 characters.
        """
        url = "http://example.com/" + "a" * 236
        self.assertEqual(validate_url(url), "Valid URL")

    def test_validate_url_valid_https_max_length(self):
        """
        Checks a valid URL with https protocol and exactly 255 characters.
        """
        url = "https://example.com/" + "a" * 235
        self.assertEqual(validate_url(url), "Valid URL")

    def test_validate_url_invalid_http_too_long(self):
        """
        Checks an invalid URL with http protocol exceeding 255 characters.
        """
        url = "http://example.com" + "a" * 238
        self.assertEqual(validate_url(url), "Invalid URL")

    def test_validate_url_invalid_https_too_long(self):
        """
        Checks an invalid URL with https protocol exceeding 255 characters.
        """
        url = "https://example.com/" + "a" * 239
        self.assertEqual(validate_url(url), "Invalid URL")

    def test_validate_url_invalid_no_protocol(self):
        """
        Checks an invalid URL without http or https protocol.
        """
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_validate_url_invalid_ftp_protocol(self):
        """
        Checks an invalid URL with ftp protocol.
        """
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_validate_url_invalid_empty_string(self):
        """
        Checks an invalid URL with empty string.
        """
        self.assertEqual(validate_url(""), "Invalid URL")

    def test_validate_url_valid_http_only(self):
        """
        Checks a valid URL with just http protocol.
        """
        self.assertEqual(validate_url("http://"), "Valid URL")

    def test_validate_url_valid_https_only(self):
        """
        Checks a valid URL with just https protocol.
        """
        self.assertEqual(validate_url("https://"), "Valid URL")

    def test_validate_url_invalid_http_uppercase(self):
        """
        Checks an invalid URL with HTTP in uppercase.
        """
        self.assertEqual(validate_url("HTTP://example.com"), "Invalid URL")

    def test_validate_url_invalid_https_uppercase(self):
        """
        Checks an invalid URL with HTTPS in uppercase.
        """
        self.assertEqual(validate_url("HTTPS://example.com"), "Invalid URL")

    def test_validate_url_invalid_contains_http_not_start(self):
        """
        Checks an invalid URL that contains http but doesn't start with it.
        """
        self.assertEqual(validate_url("www.http://example.com"), "Invalid URL")

    def test_validate_url_valid_http_with_path(self):
        """
        Checks a valid URL with http protocol and path.
        """
        self.assertEqual(validate_url("http://example.com/path/to/page"), "Valid URL")

    def test_validate_url_valid_https_with_query(self):
        """
        Checks a valid URL with https protocol and query parameters.
        """
        self.assertEqual(
            validate_url("https://example.com/page?param=value"), "Valid URL"
        )


class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    test cases for calculate quantity discount function
    """

    def test_calculate_quantity_discount_min_no_discount(self):
        """
        Checks no discount with minimum quantity.
        """
        self.assertEqual(calculate_quantity_discount(1), "No Discount")

    def test_calculate_quantity_discount_max_no_discount(self):
        """
        Checks no discount with maximum quantity for no discount tier.
        """
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_middle_no_discount(self):
        """
        Checks no discount with middle quantity in no discount tier.
        """
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_calculate_quantity_discount_min_5_percent(self):
        """
        Checks 5% discount with minimum quantity for this tier.
        """
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_calculate_quantity_discount_max_5_percent(self):
        """
        Checks 5% discount with maximum quantity for this tier.
        """
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_middle_5_percent(self):
        """
        Checks 5% discount with middle quantity in 5% discount tier.
        """
        self.assertEqual(calculate_quantity_discount(8), "5% Discount")

    def test_calculate_quantity_discount_min_10_percent(self):
        """
        Checks 10% discount with quantity just above 10.
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    def test_calculate_quantity_discount_high_10_percent(self):
        """
        Checks 10% discount with high quantity.
        """
        self.assertEqual(calculate_quantity_discount(100), "10% Discount")

    def test_calculate_quantity_discount_very_high_10_percent(self):
        """
        Checks 10% discount with very high quantity.
        """
        self.assertEqual(calculate_quantity_discount(1000), "10% Discount")

    def test_calculate_quantity_discount_zero_quantity(self):
        """
        Checks 10% discount with zero quantity.
        """
        self.assertEqual(calculate_quantity_discount(0), "10% Discount")

    def test_calculate_quantity_discount_negative_quantity(self):
        """
        Checks 10% discount with negative quantity.
        """
        self.assertEqual(calculate_quantity_discount(-5), "10% Discount")

    def test_calculate_quantity_discount_boundary_5_to_6(self):
        """
        Checks transition from no discount to 5% discount tier.
        """
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_boundary_6_to_5(self):
        """
        Checks transition to 5% discount from no discount tier.
        """
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_calculate_quantity_discount_boundary_10_to_11(self):
        """
        Checks transition from 5% discount to 10% discount tier.
        """
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_boundary_11_to_10(self):
        """
        Checks transition to 10% discount from 5% discount tier.
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")


class TestCheckFileSize(unittest.TestCase):
    """
    test cases for check file size function
    """

    def test_check_file_size_valid_zero_bytes(self):
        """
        Checks valid file size with zero bytes.
        """
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_check_file_size_valid_max_bytes(self):
        """
        Checks valid file size with exactly 1 MB.
        """
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_valid_small_file(self):
        """
        Checks valid file size with small file.
        """
        self.assertEqual(check_file_size(1024), "Valid File Size")

    def test_check_file_size_valid_medium_file(self):
        """
        Checks valid file size with medium file.
        """
        self.assertEqual(check_file_size(512000), "Valid File Size")

    def test_check_file_size_valid_near_max(self):
        """
        Checks valid file size just below maximum.
        """
        self.assertEqual(check_file_size(1048575), "Valid File Size")

    def test_check_file_size_valid_one_byte(self):
        """
        Checks valid file size with one byte.
        """
        self.assertEqual(check_file_size(1), "Valid File Size")

    def test_check_file_size_invalid_over_max(self):
        """
        Checks invalid file size with one byte over maximum.
        """
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    def test_check_file_size_invalid_negative(self):
        """
        Checks invalid file size with negative value.
        """
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_check_file_size_invalid_large_negative(self):
        """
        Checks invalid file size with large negative value.
        """
        self.assertEqual(check_file_size(-1000), "Invalid File Size")

    def test_check_file_size_invalid_much_larger(self):
        """
        Checks invalid file size with 10 MB.
        """
        self.assertEqual(check_file_size(10485760), "Invalid File Size")

    def test_check_file_size_invalid_very_large(self):
        """
        Checks invalid file size with 1 GB.
        """
        self.assertEqual(check_file_size(1073741824), "Invalid File Size")

    def test_check_file_size_valid_half_mb(self):
        """
        Checks valid file size with half MB.
        """
        self.assertEqual(check_file_size(524288), "Valid File Size")

    def test_check_file_size_valid_quarter_mb(self):
        """
        Checks valid file size with quarter MB.
        """
        self.assertEqual(check_file_size(262144), "Valid File Size")


class TestCheckLoanEligibility(unittest.TestCase):
    """
    test cases for check loan eligibilty function
    """

    def test_check_loan_eligibility_not_eligible_low_income(self):
        """
        Checks not eligible with income below 30000.
        """
        self.assertEqual(check_loan_eligibility(25000, 800), "Not Eligible")

    def test_check_loan_eligibility_not_eligible_zero_income(self):
        """
        Checks not eligible with zero income.
        """
        self.assertEqual(check_loan_eligibility(0, 750), "Not Eligible")

    def test_check_loan_eligibility_not_eligible_negative_income(self):
        """
        Checks not eligible with negative income.
        """
        self.assertEqual(check_loan_eligibility(-5000, 700), "Not Eligible")

    def test_check_loan_eligibility_not_eligible_min_boundary(self):
        """
        Checks not eligible with income just below 30000.
        """
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")

    def test_check_loan_eligibility_standard_loan_min_income_high_score(self):
        """
        Checks standard loan with minimum income and credit score above 700.
        """
        self.assertEqual(check_loan_eligibility(30000, 701), "Standard Loan")

    def test_check_loan_eligibility_standard_loan_mid_income_high_score(self):
        """
        Checks standard loan with middle income and credit score above 700.
        """
        self.assertEqual(check_loan_eligibility(45000, 750), "Standard Loan")

    def test_check_loan_eligibility_standard_loan_max_income_high_score(self):
        """
        Checks standard loan with maximum income and credit score above 700.
        """
        self.assertEqual(check_loan_eligibility(60000, 720), "Standard Loan")

    def test_check_loan_eligibility_standard_loan_min_income_boundary_score(self):
        """
        Checks standard loan with income 30000 and credit score exactly 701.
        """
        self.assertEqual(check_loan_eligibility(30000, 701), "Standard Loan")

    def test_check_loan_eligibility_secured_loan_mid_income_low_score(self):
        """
        Checks secured loan with middle income and low credit score.
        """
        self.assertEqual(check_loan_eligibility(45000, 650), "Secured Loan")

    def test_check_loan_eligibility_secured_loan_max_income_low_score(self):
        """
        Checks secured loan with maximum income and credit score at or below 700.
        """
        self.assertEqual(check_loan_eligibility(60000, 700), "Secured Loan")

    def test_check_loan_eligibility_secured_loan_very_low_score(self):
        """
        Checks secured loan with income in range and very low credit score.
        """
        self.assertEqual(check_loan_eligibility(40000, 500), "Secured Loan")

    def test_check_loan_eligibility_premium_loan_high_income_high_score(self):
        """
        Checks premium loan with income above 60000 and credit score above 750.
        """
        self.assertEqual(check_loan_eligibility(70000, 800), "Premium Loan")

    def test_check_loan_eligibility_premium_loan_min_high_income_min_high_score(self):
        """
        Checks premium loan with income just above 60000 and credit score just above 750.
        """
        self.assertEqual(check_loan_eligibility(60001, 751), "Premium Loan")

    def test_check_loan_eligibility_premium_loan_very_high_income(self):
        """
        Checks premium loan with very high income and credit score above 750.
        """
        self.assertEqual(check_loan_eligibility(100000, 800), "Premium Loan")

    def test_check_loan_eligibility_standard_loan_high_income_low_score(self):
        """
        Checks standard loan with high income but low credit score.
        """
        self.assertEqual(check_loan_eligibility(80000, 700), "Standard Loan")

    def test_check_loan_eligibility_boundary_income_30000_score_700(self):
        """
        Checks secured loan with exact boundary values.
        """
        self.assertEqual(check_loan_eligibility(30000, 700), "Secured Loan")

    def test_check_loan_eligibility_boundary_income_60000_score_750(self):
        """
        Checks standard loan with boundary income and boundary score.
        """
        self.assertEqual(check_loan_eligibility(60000, 750), "Standard Loan")


class TestCalculateShippingCost(unittest.TestCase):
    """
    test cases for calculate shipping cost function
    """

    def test_calculate_shipping_cost_5_all_max_values(self):
        """
        Checks $5 shipping with all maximum values.
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_5_weight_boundary(self):
        """
        Checks $5 shipping with weight at boundary and small dimensions.
        """
        self.assertEqual(calculate_shipping_cost(1, 5, 5, 5), 5)

    def test_calculate_shipping_cost_5_length_boundary(self):
        """
        Checks $5 shipping with length at boundary and small weight.
        """
        self.assertEqual(calculate_shipping_cost(0.5, 10, 5, 5), 5)

    def test_calculate_shipping_cost_10_all_min_values(self):
        """
        Checks $10 shipping with all minimum values for tier 2.
        """
        self.assertEqual(calculate_shipping_cost(1.1, 11, 11, 11), 10)

    def test_calculate_shipping_cost_10_all_max_values(self):
        """
        Checks $10 shipping with all maximum values for tier 2.
        """
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)

    def test_calculate_shipping_cost_10_weight_min_boundary(self):
        """
        Checks $10 shipping with weight just above 1 and dimensions in range.
        """
        self.assertEqual(calculate_shipping_cost(1.01, 20, 20, 20), 10)

    def test_calculate_shipping_cost_10_weight_max_boundary(self):
        """
        Checks $10 shipping with weight at max boundary and dimensions in range.
        """
        self.assertEqual(calculate_shipping_cost(5, 20, 20, 20), 10)

    def test_calculate_shipping_cost_10_length_min_boundary(self):
        """
        Checks $10 shipping with length at min boundary and other conditions met.
        """
        self.assertEqual(calculate_shipping_cost(3, 11, 20, 20), 10)

    def test_calculate_shipping_cost_10_length_max_boundary(self):
        """
        Checks $10 shipping with length at max boundary and other conditions met.
        """
        self.assertEqual(calculate_shipping_cost(3, 30, 20, 20), 10)

    def test_calculate_shipping_cost_20_weight_exceeds(self):
        """
        Checks $20 shipping with weight exceeding tier 2.
        """
        self.assertEqual(calculate_shipping_cost(5.1, 20, 20, 20), 20)

    def test_calculate_shipping_cost_20_length_exceeds(self):
        """
        Checks $20 shipping with length exceeding tier 2.
        """
        self.assertEqual(calculate_shipping_cost(3, 31, 20, 20), 20)

    def test_calculate_shipping_cost_20_width_exceeds(self):
        """
        Checks $20 shipping with width exceeding tier 2.
        """
        self.assertEqual(calculate_shipping_cost(3, 20, 31, 20), 20)

    def test_calculate_shipping_cost_20_height_exceeds(self):
        """
        Checks $20 shipping with height exceeding tier 2.
        """
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 31), 20)

    def test_calculate_shipping_cost_20_all_exceed(self):
        """
        Checks $20 shipping with all parameters exceeding tier 2.
        """
        self.assertEqual(calculate_shipping_cost(10, 50, 50, 50), 20)

    def test_calculate_shipping_cost_20_weight_below_tier2_dims_exceed(self):
        """
        Checks $20 shipping with weight in tier 2 but dimensions exceeding.
        """
        self.assertEqual(calculate_shipping_cost(3, 50, 50, 50), 20)

    def test_calculate_shipping_cost_20_weight_exceeds_dims_in_tier2(self):
        """
        Checks $20 shipping with weight exceeding but dimensions in tier 2 range.
        """
        self.assertEqual(calculate_shipping_cost(6, 20, 20, 20), 20)

    def test_calculate_shipping_cost_20_weight_tier1_one_dim_exceeds(self):
        """
        Checks $20 shipping with tier 1 weight but one dimension exceeds tier 1.
        """
        self.assertEqual(calculate_shipping_cost(1, 11, 5, 5), 20)

    def test_calculate_shipping_cost_20_weight_tier2_one_dim_below(self):
        """
        Checks $20 shipping with tier 2 weight but one dimension below tier 2 minimum.
        """
        self.assertEqual(calculate_shipping_cost(3, 10, 20, 20), 20)

    def test_calculate_shipping_cost_20_negative_weight(self):
        """
        Checks $20 shipping with negative weight.
        """
        self.assertEqual(calculate_shipping_cost(-1, 20, 20, 20), 20)

    def test_calculate_shipping_cost_20_negative_dimension(self):
        """
        Checks $20 shipping with negative dimension.
        """
        self.assertEqual(calculate_shipping_cost(1, -5, 5, 5), 20)
