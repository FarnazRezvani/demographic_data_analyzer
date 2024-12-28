import unittest
from demographic_data_analyzer import calculate_race_counts, calculate_average_age_men

class TestDemographicDataAnalyzer(unittest.TestCase):

    def test_race_counts(self):
        result = calculate_race_counts()
        expected_result = {'White': 27816, 'Black': 3124, 'Asian-Pac-Islander': 1039, 'Amer-Indian-Eskimo': 311, 'Other': 271}
        self.assertEqual(result.to_dict(), expected_result)

    def test_average_age_men(self):
        result = calculate_average_age_men()
        expected_result = 39.43
        self.assertAlmostEqual(result, expected_result, places=2)

if __name__ == '__main__':
    unittest.main()