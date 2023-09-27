import unittest
from weatherForecast import weatherForTheWeek

class testCase2(unittest.TestCase):
    def test_weatherForecast(self):
        self.assertEqual(weatherForTheWeek(), "us") 
        #USING
        # context = ssl._create_unverified_context()
        # response = urlopen(forecastURL(), context=context)
        # weatherData = json.loads(response.read())
        # return weatherData["properties"]["units"]
    
if __name__ == '__main__':
    unittest.main()

    
        


