[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12065937&assignment_repo_type=AssignmentRepo)
# Assignment 4
1. Write a Python program that uses NOAA web service endpoints to display the 7-day forecast for Muncie (lat: 40.1934, lon: -85.3864). The first web service endpoint that you will seek is https://api.weather.gov/points/40.1934,-85.3864

2. Look for the value of the 'forecast' key within the 'properties' object of the JSON that is returned.

3. This value should be used as the second web service endpoint to seek the 7-day 12-hour forecast. The 'periods' list within the 'properties' object contains 14 JSON objects (two for each day). 

4. Your program should display the values of the keys 'name'. 'temperature', and 'detailedForecast' for all 14 JSON objects.

5. There is no user input to your program.

6. You MUST include at least two unit tests as part of your code.
