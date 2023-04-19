# CortevaCodingExercise
A sample project for Corteva Coding Exercise 

### Problem 1 - Data Modeling:

* Answer location: sql/Weather.sql
* Description: created a MySQL table locally to contain all the data with a primary key combo of [Location, DateStamp] to make sure uniqueness

### Problem 2 - Ingestion:
* Answer location: data-import-process/importer.py
* Description: created a process that read through all the files in certain folder and parse and insert into MySQL DB table. It will log according to different levels as well

### Problem 3 - Data Analysis:
* Answer location: data-analysis/stats.py + WeatherStat.sql
* Description:
  * created a MySQL table locally to contain all the data with a primary key combo of [Location, Year] to make sure uniqueness 
  * created 1 method to execute stored procedure in MySQL DB to calculate stats and put the result into WeatherStats table

### Problem 4 - REST API:
* Answer location: api/
* Description: created DJango REST API by following online tutorial that contains 
  * a swagger page that contains all endpoints "/docs"
  * A few API endpoints in apis.py with some dummy logging
    * apis/weather: this will return all weather data if no parameter passed, with parameter, it will select data of certain location/year/page
      * Sample link: http://127.0.0.1:8000/apis/weather?location=USC00110072&year=1985&page=100
    * apis/stats: this will return all weather stats data if no parameter passed, with parameter, it will select data of certain location/year
      * Sample link: http://127.0.0.1:8000/apis/weather/stats?location=USC00110072&year=1985&page=100
  * Integration Test cases in test/test_api.py

### Deployment:
* for API:
  * using below components:
    * (Required) Database: RDS (Relational Database Service) for MySQL db
    * (Required) Instance hosting: EC2 (Elastic Compute Cloud)
    * (Required) Secure the access of AWS: IAM (Identity and Access Management)
    * (Recommended) Logging: we can use file storage service like S3 to store the logs or we can call CloudWatch 
    * (Optional) Route 53: to register and map DNS (maybe not needed if this is for internal usage)
    * (Optional) Load balancer: maybe not need if the traffic is low, we can use ELB (Elastic Load Balancer)
    * (Optional) traffic control: (if not internal only) we can use Virtual Private Cloud (VPC) to isolate resources and control inbound and outbound traffic
* for data ingestion:
  * Logic layer: since it's just 1 function, we can just use serverless architecture to handle it
  * File storage: we can use S3 to store the input data files
  * Task Scheduling: we can use Amazon EventBridge Scheduler for task scheduling process (Tutorial: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html)