import unittest
from unittest.mock import patch
from ICE2_100611292 import validate_temperature, process_temperatures, main

class TestTemperatureFunctions(unittest.TestCase):

    def test_validate_temperature_valid(self):
        self.assertEqual(validate_temperature("25"), 25.0)
        self.assertEqual(validate_temperature("-10"), -10.0)
        self.assertEqual(validate_temperature("150"), 150.0)

    def test_validate_temperature_empty_string(self):
        self.assertIsNone(validate_temperature(""))  #

    def test_validate_temperature_out_of_range(self):
        self.assertEqual(validate_temperature("-100"), "Out of range value has been detected: -100")
        self.assertEqual(validate_temperature("200"), "Out of range value has been detected: 200")

    def test_validate_temperature_invalid_input(self):
        self.assertEqual(validate_temperature("abc"), "Invalid input detected: abc")
        self.assertEqual(validate_temperature("12abc"), "Invalid input detected: 12abc")

    ## ✅ TEST CASES FOR process_temperatures ##
    def test_process_temperatures_integer_avg(self):
        self.assertEqual(process_temperatures([10, 20, 30]), "Min: 10°C, Max: 30°C, Avg: 20°C")

    def test_process_temperatures_decimal_avg(self):
        self.assertEqual(process_temperatures([10, 15, 30]), "Min: 10°C, Max: 30°C, Avg: 18°C")

    def test_process_temperatures_all_same_values(self):
        self.assertEqual(process_temperatures([25, 25, 25]), "Min: 25°C, Max: 25°C, Avg: 25°C")


    def test_process_temperatures_min_max(self):
        self.assertEqual(process_temperatures([-50, 0, 150]), "Min: -50°C, Max: 150°C, Avg: 33°C")

    def test_process_temperatures_close_to_max(self):
        self.assertEqual(process_temperatures([149.9, 150, 150]), "Min: 149.9°C, Max: 150°C, Avg: 150°C")

    @patch("builtins.input", side_effect=["10", "20", "30"])
    @patch("builtins.print")
    def test_main_valid_inputs(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Min: 10°C, Max: 30°C, Avg: 20°C")

    @patch("builtins.input", side_effect=["-100", "abc", "200"])
    @patch("builtins.print")
    def test_main_invalid_inputs(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Out of range value has been detected: -100")
        mock_print.assert_any_call("Invalid input detected: abc")
        mock_print.assert_any_call("Out of range value has been detected: 200")

    @patch("builtins.input", side_effect=["", "", ""])
    @patch("builtins.print")
    def test_main_no_input_provided(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("No input provided, Please try again.")

    @patch("builtins.input", side_effect=["10", "abc", "20"])
    @patch("builtins.print")
    def test_main_mixed_valid_invalid_inputs(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Invalid input detected: abc")
        mock_print.assert_any_call("Min: 10°C, Max: 20°C, Avg: 15°C")

    @patch("builtins.input", side_effect=["10", "20", "30"])
    @patch("builtins.print")
    def test_main_direct_execution(self, mock_print, mock_input):

        import ICE2_100611292
        ICE2_100611292.__name__ = "__main__"
        ICE2_100611292.main()
        mock_print.assert_called_with("Min: 10°C, Max: 30°C, Avg: 20°C")

if __name__ == "__main__":
    unittest.main()


