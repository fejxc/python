from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    customer_ID = int(fields[0])
    amount_spent = float(fields[2])
    return ( customer_ID, amount_spent)

lines = sc.textFile("file:///Users/sunyun/Downloads/SparkCourse/customer-orders.csv")
rdd = lines.map(parseLine)
totalsByCustomer = rdd.reduceByKey(lambda x, y: x + y)
totalsByCustomer_sorted = totalsByCustomer.map(lambda x: (x[1], x[0])).sortByKey()
results = totalsByCustomer_sorted.collect()
for result in results:
    print(result)
