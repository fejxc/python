from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StuCount").getOrCreate()

people = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("hdfs://localhost:8020/user/sunyun/StuCount")
    
print("Here is our inferred schema:")
people.printSchema()

print("Average friends by age")



people.groupBy("学号").agg({"学号":"count"}).sort("学号").show(100)


spark.stop()

