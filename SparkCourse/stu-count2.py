from pyspark import SparkConf, SparkContext
import codecs
def loadStuNames():
    stuNames = {}
    with open("/Users/sunyun/Downloads/SparkCourse/18-3_20210512_12_no_head.csv",'r',encoding = "UTF-8") as f:
        for line in f:
            fields = line.split(',')
            stuNames[int(fields[0])] = fields[1]
    return stuNames

def parseInput(line):
    fields = line.split(',')
    return (( int(fields[0]), 1))

if __name__ == "__main__":
    
    conf = SparkConf().setAppName("WorstMovies")
    sc = SparkContext(conf = conf)

    stuNames = loadStuNames()

    lines = sc.textFile("hdfs://localhost:8020/user/sunyun/input/18-3_20210512_12_no_head.csv")

    stuCount = lines.map(parseInput)

    Count = stuCount.reduceByKey(lambda x, y: x + y)


    sortedMovies = Count.sortBy(lambda x: x[0])

    results = sortedMovies.take(50)

    for result in results:
        print(result[0], result[1])
    for result in results:
        print(stuNames[result[0]], result[1])
