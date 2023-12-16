import unittest
import time
from time_helper import Timer

class TestTimer(unittest.TestCase):
    def setUp(self):
        self.timer = Timer()

    def test_count(self):
        self.timer.count()
        self.assertEqual(len(self.timer.end_times), 1)

    def test_diff(self):
        self.timer.count()
        time.sleep(1)
        self.timer.count()
        self.assertAlmostEqual(self.timer.diff(), 1, places=1)

    def test_diff_str(self):
        self.timer.count()
        time.sleep(1)
        self.timer.count()
        print(f'diff_str: {self.timer.diff_str()}')
        self.assertTrue(isinstance(self.timer.diff_str(), str))

    def test_duration(self):
        new_timer = Timer()
        time.sleep(1)
        new_timer.count()
        time.sleep(1)
        new_timer.count()
        time.sleep(1)
        new_timer.count()
        self.assertAlmostEqual(new_timer.duration(), 3, places=1)

    def test_duration_str(self):
        self.timer.count()
        time.sleep(1)
        self.timer.count()
        print(f'diff_str: {self.timer.duration_str()}')
        self.assertTrue(isinstance(self.timer.duration_str(), str))

    def test_format_time(self):
        formatted_time = self.timer.format_time(1.234567)
        self.assertEqual(formatted_time, '1.23 sec')

    def test_min_timer(self):
        min_timer = Timer(unit='min', precision=4) 
        time.sleep(0.42)
        print(min_timer.count().diff_str())

    def test_ms_timer(self):
        ms_timer = Timer(unit='ms', precision=1) 
        time.sleep(0.42)
        print(ms_timer.count().diff_str())

if __name__ == '__main__':
    unittest.main()
