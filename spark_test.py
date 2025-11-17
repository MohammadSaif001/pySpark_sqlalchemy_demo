import findspark
findspark.init()

from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("SaifApp") \
    .config("spark.jars.packages", "org.xerial:sqlite-jdbc:3.45.3.0") \
    .getOrCreate()

print("Spark session created successfully.")

df = spark.read.format("jdbc").options(
    url="jdbc:sqlite:mydatabase.db",
    dbtable="students",
    driver="org.sqlite.JDBC"
).load()

df.show()
spark.stop()