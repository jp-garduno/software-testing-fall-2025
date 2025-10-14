# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    DocumentEditingSystem,
    ElevatorSystem,
    UserAuthentication,
)


class TestUserAuthentication(unittest.TestCase):
    """
    UserAuthentication unit tests.
    """

    def setUp(self):
        """
        Set up a fresh UserAuthentication instance before each test.
        """
        self.user_auth = UserAuthentication()

    def test_user_authentication_initial_state(self):
        """
        Checks that user authentication starts in 'Logged Out' state.
        """
        self.assertEqual(self.user_auth.state, "Logged Out")

    def test_user_authentication_login_from_logged_out(self):
        """
        Checks successful login from 'Logged Out' state.
        """
        output = self.user_auth.login()
        self.assertEqual(self.user_auth.state, "Logged In")
        self.assertEqual(output, "Login successful")

    def test_user_authentication_login_from_logged_in(self):
        """
        Checks that login fails when already in 'Logged In' state.
        """
        self.user_auth.login()
        output = self.user_auth.login()
        self.assertEqual(self.user_auth.state, "Logged In")
        self.assertEqual(output, "Invalid operation in current state")

    def test_user_authentication_multiple_login_attempts(self):
        """
        Checks multiple consecutive login attempts.
        """
        output1 = self.user_auth.login()
        self.assertEqual(output1, "Login successful")
        self.assertEqual(self.user_auth.state, "Logged In")

        output2 = self.user_auth.login()
        self.assertEqual(output2, "Invalid operation in current state")
        self.assertEqual(self.user_auth.state, "Logged In")

    def test_user_authentication_logout_from_logged_in(self):
        """
        Checks successful logout from 'Logged In' state.
        """
        self.user_auth.login()
        output = self.user_auth.logout()
        self.assertEqual(self.user_auth.state, "Logged Out")
        self.assertEqual(output, "Logout successful")

    def test_user_authentication_logout_from_logged_out(self):
        """
        Checks that logout fails when already in 'Logged Out' state.
        """
        output = self.user_auth.logout()
        self.assertEqual(self.user_auth.state, "Logged Out")
        self.assertEqual(output, "Invalid operation in current state")

    def test_user_authentication_multiple_logout_attempts(self):
        """
        Checks multiple consecutive logout attempts.
        """
        self.user_auth.login()

        output1 = self.user_auth.logout()
        self.assertEqual(output1, "Logout successful")
        self.assertEqual(self.user_auth.state, "Logged Out")

        output2 = self.user_auth.logout()
        self.assertEqual(output2, "Invalid operation in current state")
        self.assertEqual(self.user_auth.state, "Logged Out")

    def test_user_authentication_login_logout_cycle(self):
        """
        Checks complete login-logout cycle transitions correctly.
        """
        self.assertEqual(self.user_auth.state, "Logged Out")

        output1 = self.user_auth.login()
        self.assertEqual(output1, "Login successful")
        self.assertEqual(self.user_auth.state, "Logged In")

        output2 = self.user_auth.logout()
        self.assertEqual(output2, "Logout successful")
        self.assertEqual(self.user_auth.state, "Logged Out")


class TestDocumentEditingSystem(unittest.TestCase):
    """
    DocumentEditingSystem unit tests.
    """

    def setUp(self):
        """
        Set up a fresh DocumentEditingSystem instance before each test.
        """
        self.doc_system = DocumentEditingSystem()

    def test_document_editing_system_initial_state(self):
        """
        Checks that document editing system starts in 'Editing' state.
        """
        self.assertEqual(self.doc_system.state, "Editing")

    def test_document_editing_system_save_from_editing(self):
        """
        Checks successful save from 'Editing' state.
        """
        output = self.doc_system.save_document()
        self.assertEqual(self.doc_system.state, "Saved")
        self.assertEqual(output, "Document saved successfully")

    def test_document_editing_system_save_from_saved(self):
        """
        Checks that save fails when already in 'Saved' state.
        """
        self.doc_system.save_document()
        output = self.doc_system.save_document()
        self.assertEqual(self.doc_system.state, "Saved")
        self.assertEqual(output, "Invalid operation in current state")

    def test_document_editing_system_multiple_save_attempts(self):
        """
        Checks multiple consecutive save attempts.
        """
        output1 = self.doc_system.save_document()
        self.assertEqual(output1, "Document saved successfully")
        self.assertEqual(self.doc_system.state, "Saved")

        output2 = self.doc_system.save_document()
        self.assertEqual(output2, "Invalid operation in current state")
        self.assertEqual(self.doc_system.state, "Saved")

    def test_document_editing_system_edit_from_saved(self):
        """
        Checks successful edit from 'Saved' state.
        """
        self.doc_system.save_document()
        output = self.doc_system.edit_document()
        self.assertEqual(self.doc_system.state, "Editing")
        self.assertEqual(output, "Editing resumed")

    def test_document_editing_system_edit_from_editing(self):
        """
        Checks that edit fails when already in 'Editing' state.
        """
        output = self.doc_system.edit_document()
        self.assertEqual(self.doc_system.state, "Editing")
        self.assertEqual(output, "Invalid operation in current state")

    def test_document_editing_system_multiple_edit_attempts(self):
        """
        Checks multiple consecutive edit attempts.
        """
        self.doc_system.save_document()

        output1 = self.doc_system.edit_document()
        self.assertEqual(output1, "Editing resumed")
        self.assertEqual(self.doc_system.state, "Editing")

        output2 = self.doc_system.edit_document()
        self.assertEqual(output2, "Invalid operation in current state")
        self.assertEqual(self.doc_system.state, "Editing")

    def test_document_editing_system_save_edit_cycle(self):
        """
        Checks complete save-edit cycle transitions correctly.
        """
        self.assertEqual(self.doc_system.state, "Editing")

        output1 = self.doc_system.save_document()
        self.assertEqual(output1, "Document saved successfully")
        self.assertEqual(self.doc_system.state, "Saved")

        output2 = self.doc_system.edit_document()
        self.assertEqual(output2, "Editing resumed")
        self.assertEqual(self.doc_system.state, "Editing")


class TestElevatorSystem(unittest.TestCase):
    """
    ElevatorSystem unit tests.
    """

    def setUp(self):
        """
        Set up a fresh ElevatorSystem instance before each test.
        """
        self.elevator = ElevatorSystem()

    def test_elevator_system_initial_state(self):
        """
        Checks that elevator system starts in 'Idle' state.
        """
        self.assertEqual(self.elevator.state, "Idle")

    def test_elevator_system_move_up_from_idle(self):
        """
        Checks successful move up from 'Idle' state.
        """
        output = self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(output, "Elevator moving up")

    def test_elevator_system_move_up_from_moving_up(self):
        """
        Checks that move up fails when already in 'Moving Up' state.
        """
        self.elevator.move_up()
        output = self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(output, "Invalid operation in current state")

    def test_elevator_system_move_up_from_moving_down(self):
        """
        Checks that move up fails when in 'Moving Down' state.
        """
        self.elevator.move_down()
        output = self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(output, "Invalid operation in current state")

    def test_elevator_system_move_down_from_idle(self):
        """
        Checks successful move down from 'Idle' state.
        """
        output = self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(output, "Elevator moving down")

    def test_elevator_system_move_down_from_moving_down(self):
        """
        Checks that move down fails when already in 'Moving Down' state.
        """
        self.elevator.move_down()
        output = self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(output, "Invalid operation in current state")

    def test_elevator_system_move_down_from_moving_up(self):
        """
        Checks that move down fails when in 'Moving Up' state.
        """
        self.elevator.move_up()
        output = self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(output, "Invalid operation in current state")

    def test_elevator_system_stop_from_moving_up(self):
        """
        Checks successful stop from 'Moving Up' state.
        """
        self.elevator.move_up()
        output = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_elevator_system_stop_from_moving_down(self):
        """
        Checks successful stop from 'Moving Down' state.
        """
        self.elevator.move_down()
        output = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_elevator_system_stop_from_idle(self):
        """
        Checks that stop fails when already in 'Idle' state.
        """
        output = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(output, "Invalid operation in current state")

    def test_elevator_system_multiple_stop_attempts_from_idle(self):
        """
        Checks multiple consecutive stop attempts from idle.
        """
        output1 = self.elevator.stop()
        self.assertEqual(output1, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Idle")

        output2 = self.elevator.stop()
        self.assertEqual(output2, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Idle")

    def test_elevator_system_move_up_stop_cycle(self):
        """
        Checks complete move up-stop cycle transitions correctly.
        """
        self.assertEqual(self.elevator.state, "Idle")

        output1 = self.elevator.move_up()
        self.assertEqual(output1, "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

        output2 = self.elevator.stop()
        self.assertEqual(output2, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_elevator_system_move_down_stop_cycle(self):
        """
        Checks complete move down-stop cycle transitions correctly.
        """
        self.assertEqual(self.elevator.state, "Idle")

        output1 = self.elevator.move_down()
        self.assertEqual(output1, "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

        output2 = self.elevator.stop()
        self.assertEqual(output2, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_elevator_system_alternating_up_down_cycles(self):
        """
        Checks alternating move up and move down cycles.
        """
        self.elevator.move_up()
        self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")

        self.elevator.move_down()
        self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")

        self.elevator.move_up()
        self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")

    def test_elevator_system_alternating_valid_invalid_operations(self):
        """
        Checks alternating valid and invalid operations.
        """
        output1 = self.elevator.move_up()
        self.assertEqual(output1, "Elevator moving up")

        output2 = self.elevator.move_up()
        self.assertEqual(output2, "Invalid operation in current state")

        output3 = self.elevator.stop()
        self.assertEqual(output3, "Elevator stopped")

        output4 = self.elevator.stop()
        self.assertEqual(output4, "Invalid operation in current state")

    def test_elevator_system_cannot_change_direction_without_stop(self):
        """
        Checks that elevator cannot change direction without stopping first.
        """
        self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Up")

        output = self.elevator.move_down()
        self.assertEqual(output, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Up")


if __name__ == "__main__":
    unittest.main()
