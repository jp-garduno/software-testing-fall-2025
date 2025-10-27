# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    authenticate_user,
    get_weather_advisory,
    grade_quiz,
)


class TestGradeQuiz(unittest.TestCase):
    """
    test cases for grade quiz function
    """

    def test_grade_quiz_pass_min_correct_min_incorrect(self):
        """
        Checks pass with minimum correct answers and minimum incorrect.
        """
        self.assertEqual(grade_quiz(7, 0), "Pass")

    def test_grade_quiz_pass_min_correct_max_incorrect(self):
        """
        Checks pass with minimum correct answers and maximum incorrect.
        """
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_grade_quiz_pass_high_correct_no_incorrect(self):
        """
        Checks pass with high correct answers and no incorrect.
        """
        self.assertEqual(grade_quiz(10, 0), "Pass")

    def test_grade_quiz_pass_high_correct_max_incorrect(self):
        """
        Checks pass with high correct answers and maximum incorrect.
        """
        self.assertEqual(grade_quiz(10, 2), "Pass")

    def test_grade_quiz_pass_mid_correct_one_incorrect(self):
        """
        Checks pass with middle correct answers and one incorrect.
        """
        self.assertEqual(grade_quiz(8, 1), "Pass")

    def test_grade_quiz_conditional_pass_min_correct_no_incorrect(self):
        """
        Checks conditional pass with minimum correct and no incorrect.
        """
        self.assertEqual(grade_quiz(5, 0), "Conditional Pass")

    def test_grade_quiz_conditional_pass_min_correct_max_incorrect(self):
        """
        Checks conditional pass with minimum correct and maximum incorrect.
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_grade_quiz_conditional_pass_six_correct_three_incorrect(self):
        """
        Checks conditional pass with 6 correct and 3 incorrect.
        """
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")

    def test_grade_quiz_fail_low_correct_no_incorrect(self):
        """
        Checks fail with correct answers below 5 and no incorrect.
        """
        self.assertEqual(grade_quiz(4, 0), "Fail")

    def test_grade_quiz_fail_low_correct_high_incorrect(self):
        """
        Checks fail with low correct and high incorrect.
        """
        self.assertEqual(grade_quiz(3, 5), "Fail")

    def test_grade_quiz_fail_min_correct_too_many_incorrect(self):
        """
        Checks fail with minimum correct but too many incorrect.
        """
        self.assertEqual(grade_quiz(5, 4), "Fail")

    def test_grade_quiz_fail_pass_correct_too_many_incorrect(self):
        """
        Checks fail with pass-level correct but too many incorrect.
        """
        self.assertEqual(grade_quiz(7, 3), "Fail")

    def test_grade_quiz_fail_high_correct_too_many_incorrect(self):
        """
        Checks fail with high correct but too many incorrect.
        """
        self.assertEqual(grade_quiz(10, 4), "Fail")

    def test_grade_quiz_fail_zero_correct_zero_incorrect(self):
        """
        Checks fail with zero correct and zero incorrect.
        """
        self.assertEqual(grade_quiz(0, 0), "Fail")

    def test_grade_quiz_fail_zero_correct_some_incorrect(self):
        """
        Checks fail with zero correct and some incorrect.
        """
        self.assertEqual(grade_quiz(0, 5), "Fail")

    def test_grade_quiz_fail_just_below_conditional_correct(self):
        """
        Checks fail with correct just below conditional threshold.
        """
        self.assertEqual(grade_quiz(4, 2), "Fail")

    def test_grade_quiz_boundary_conditional_to_fail_correct(self):
        """
        Checks boundary where 4 correct with 3 incorrect is fail.
        """
        self.assertEqual(grade_quiz(4, 3), "Fail")

    def test_grade_quiz_negative_correct(self):
        """
        Checks fail with negative correct answers.
        """
        self.assertEqual(grade_quiz(-1, 2), "Fail")

    def test_grade_quiz_negative_incorrect(self):
        """
        Checks result with negative incorrect answers.
        """
        self.assertEqual(grade_quiz(7, -1), "Pass")


class TestAuthenticateUser(unittest.TestCase):
    """
    test cases for authenticate user function
    """

    def test_authenticate_user_admin_correct_credentials(self):
        """
        Checks admin authentication with correct username and password.
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_admin_wrong_password(self):
        """
        Checks authentication fails with admin username but wrong password.
        """
        self.assertEqual(authenticate_user("admin", "wrongpass"), "Invalid")

    def test_authenticate_user_admin_username_wrong_case(self):
        """
        Checks authentication with admin username in wrong case (case-sensitive).
        """
        self.assertEqual(authenticate_user("Admin", "admin123"), "Invalid")

    def test_authenticate_user_admin_password_wrong_case(self):
        """
        Checks authentication with admin password in wrong case (case-sensitive).
        """
        self.assertEqual(authenticate_user("admin", "Admin123"), "Invalid")

    def test_authenticate_user_admin_empty_password(self):
        """
        Checks authentication fails with admin username but empty password.
        """
        self.assertEqual(authenticate_user("admin", ""), "Invalid")

    def test_authenticate_user_user_min_length(self):
        """
        Checks user authentication with minimum valid lengths.
        """
        self.assertEqual(authenticate_user("user1", "password"), "User")

    def test_authenticate_user_user_exact_min_username(self):
        """
        Checks user authentication with exact minimum username length.
        """
        self.assertEqual(authenticate_user("abcde", "password123"), "User")

    def test_authenticate_user_user_exact_min_password(self):
        """
        Checks user authentication with exact minimum password length.
        """
        self.assertEqual(authenticate_user("username", "pass1234"), "User")

    def test_authenticate_user_invalid_username_too_short(self):
        """
        Checks invalid authentication with username below 5 characters.
        """
        self.assertEqual(authenticate_user("user", "password123"), "Invalid")

    def test_authenticate_user_invalid_password_too_short(self):
        """
        Checks invalid authentication with password below 8 characters.
        """
        self.assertEqual(authenticate_user("username", "pass123"), "Invalid")

    def test_authenticate_user_invalid_empty_username(self):
        """
        Checks invalid authentication with empty username.
        """
        self.assertEqual(authenticate_user("", "password123"), "Invalid")

    def test_authenticate_user_invalid_empty_password(self):
        """
        Checks invalid authentication with empty password.
        """
        self.assertEqual(authenticate_user("username", ""), "Invalid")

    def test_authenticate_user_invalid_both_empty(self):
        """
        Checks invalid authentication with both username and password empty.
        """
        self.assertEqual(authenticate_user("", ""), "Invalid")

    def test_authenticate_user_boundary_password_7_chars(self):
        """
        Checks invalid with password at 7 characters.
        """
        self.assertEqual(authenticate_user("username", "pass123"), "Invalid")

    def test_authenticate_user_admin_with_spaces(self):
        """
        Checks authentication fails with admin username/password containing spaces.
        """
        self.assertEqual(authenticate_user("admin ", "admin123"), "Invalid")

    def test_authenticate_user_admin_substring_in_username(self):
        """
        Checks user authentication when username contains 'admin' but is not exactly 'admin'.
        """
        self.assertEqual(authenticate_user("adminuser", "admin123"), "Invalid")

    def test_authenticate_user_admin_substring_in_password(self):
        """
        Checks authentication when password contains 'admin123' but username is not 'admin'.
        """
        self.assertEqual(authenticate_user("username", "admin123"), "Invalid")

    def test_authenticate_user_long_admin_like_credentials(self):
        """
        Checks user authentication with credentials similar to admin but meeting user criteria.
        """
        self.assertEqual(authenticate_user("administrator", "admin123456"), "User")


class TestGetWeatherAvisory(unittest.TestCase):
    """
    test cases for get weather avisory function
    """

    def test_get_weather_advisory_high_temp_high_humidity_min_values(self):
        """
        Checks high temp/humidity advisory with minimum qualifying values.
        """
        self.assertEqual(
            get_weather_advisory(31, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_low_temp_zero(self):
        """
        Checks low temperature advisory at the minimum qualifying value.
        """
        self.assertEqual(get_weather_advisory(-1, 50), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_high_temp_boundary_humidity(self):
        """
        Temp just over limit, but humidity at limit.
        """
        self.assertEqual(get_weather_advisory(31, 70), "No Specific Advisory")

    def test_get_weather_advisory_boundary_temp_high_humidity(self):
        """
        Temp at limit, but humidity just over limit.
        """
        self.assertEqual(get_weather_advisory(30, 71), "No Specific Advisory")

    def test_get_weather_advisory_both_at_boundary(self):
        """
        Both values at limit.
        """
        self.assertEqual(get_weather_advisory(30, 70), "No Specific Advisory")

    def test_get_weather_advisory_high_temp_boundary_minus_one(self):
        """
        Temp at limit, humidity high.
        """
        self.assertEqual(get_weather_advisory(30, 80), "No Specific Advisory")

    def test_get_weather_advisory_high_humidity_boundary_minus_one(self):
        """
        Temp high, humidity at limit.
        """
        self.assertEqual(get_weather_advisory(35, 70), "No Specific Advisory")

    def test_get_weather_advisory_zero_temp(self):
        """
        Temperature at low temp boundary.
        """
        self.assertEqual(get_weather_advisory(0, 50), "No Specific Advisory")

    def test_get_weather_advisory_priority_low_temp_over_high_conditions(self):
        """
        Checks that low temperature advisory takes priority over high temp/humidity.
        """
        self.assertEqual(get_weather_advisory(-5, 75), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_low_temp_high_humidity(self):
        """
        Checks low temperature advisory even with high humidity.
        """
        self.assertEqual(get_weather_advisory(-1, 80), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_negative_humidity(self):
        """
        Checks low temperature advisory with negative temperature and negative humidity.
        """
        self.assertEqual(get_weather_advisory(-5, -10), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_very_high_humidity(self):
        """
        Checks no advisory with normal temp but too high humidity.
        """
        self.assertEqual(get_weather_advisory(25, 100), "No Specific Advisory")
