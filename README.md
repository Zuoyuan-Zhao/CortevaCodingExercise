# CortevaCodingExercise
A sample project for Corteva Coding Exercise 

### Problem 1 - Data Modeling:

* Answer location: sql/Weather.sql
* Description: created a MySQL table locally to contain all the data with a primary key combo of [Location, DateStamp] to make sure uniqueness

### Problem 2 - Ingestion:
* Answer location: data-import-process/importer.py
* Description: created a process that read through all the files in certain folder and parse and insert into MySQL DB table. It will log according to different levels as well

### Problem 3 - Data Analysis:
* Answer location: data-analysis/stats.py
* Description: created 2 method to execute queries in MySQL DB, which requires parameters from user and will output result directly

### Problem 4 - REST API:
* Answer location: api/
* Description: created DJango REST API by following online tutorial that contains 
  * a swagger page that contains all endpoints "/docs"
  * A few API endpoints in apis.py
    * apis/weather: this will return all weather data if no parameter passed, with parameter, it will select data of certain location/year/page
    * apis/stats/min_avg: this will return average of min temperatures of certain year and location
    * apis/stats/max_avg: this will return average of max temperatures of certain year and location