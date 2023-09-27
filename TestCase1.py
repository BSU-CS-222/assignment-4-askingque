import unittest
from weatherForecast import forecastURL

class testCase1(unittest.TestCase):
    def test_forecastURL(self):
        self.assertEqual(forecastURL(), "https://api.weather.gov/gridpoints/IND/83,90/forecast") #manually grabbed URL to test if that is what was returning

if __name__ == '__main__':
    unittest.main()