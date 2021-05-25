from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

people = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("file:///Users/sunyun/Downloads/SparkCourse/fakefriends-header.csv")
    
print("Here is our inferred schema:")
people.printSchema()

print("Average friends by age")
people.select("age","friends").groupBy("age").avg("friends").sort("age").show()

spark.stop()

