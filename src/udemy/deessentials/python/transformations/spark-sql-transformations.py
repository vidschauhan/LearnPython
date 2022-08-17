# Created by vidit.singh at 24-06-2022

from pyspark.sql import SparkSession
import getpass

username = 'itversity'
print(username)
from pyspark import SparkConf, SparkContext

sc = SparkContext(master="local", appName="Spark Demo")
print(sc.textFile("D:\\vidit.txt").first())

orderItems = sc.textFile("/mnt/c/Users/vidit.singh/Downloads/part-00000.txt")