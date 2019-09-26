import unittest

from versionanalyzer.utilities import VersionChecker


class TestVersionAnalyzer(unittest.TestCase):
    """ Test Version between two version to see which one is greater"""

    def test_check_version_is_greater(self):
        version_one = "1.2"
        version_two = "1.5"
        version_checker = VersionChecker()
        result = version_checker.check_version(version_one, version_two)
        self.assertEqual(result, False)

    def test_check_version_is_lower(self):
        version_one = "1.8"
        version_two = "1.5"
        version_checker = VersionChecker()
        result = version_checker.check_version(version_one, version_two)
        self.assertEqual(result, True)
