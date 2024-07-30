import unittest
from unittest.mock import patch, MagicMock
from pybp.logger.app_logger import AppLogger, get_logger


class TestAppLogger(unittest.TestCase):
    def setUp(self):
        self.logger = get_logger()

    @patch('logging.Logger.debug')
    def test_debug_logging(self, mock_debug):
        message = "Test debug message"
        self.logger.debug(message)
        mock_debug.assert_called_once()

    @patch('logging.Logger.info')
    def test_info_logging(self, mock_info):
        message = "Test info message"
        self.logger.info(message)
        mock_info.assert_called_once()

    @patch('logging.Logger.warning')
    def test_warning_logging(self, mock_warning):
        message = "Test warning message"
        self.logger.warning(message)
        mock_warning.assert_called_once()

    @patch('logging.Logger.error')
    def test_error_logging(self, mock_error):
        message = "Test error message"
        self.logger.error(message)
        mock_error.assert_called_once()

    @patch('logging.Logger.critical')
    def test_critical_logging(self, mock_critical):
        message = "Test critical message"
        self.logger.crit(message)
        mock_critical.assert_called_once()


if __name__ == '__main__':
    unittest.main()
