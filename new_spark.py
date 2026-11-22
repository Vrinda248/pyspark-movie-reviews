from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length

spark = SparkSession.builder.appName("IMDb").getOrCreate()
# 1. Load
df = spark.read.csv("IMDB Dataset.csv", header=True, inferSchema=True, multiLine=True, quote='"', escape='"')

# 2. Explore
df.printSchema()
df.show(5)

# 3. Clean
df = df.filter(col("review").isNotNull() & (col("review") != ""))
#df = df.dropDuplicates(["review"])

# 4. Analyze
print("Total reviews:", df.count())
pos_no=df.filter(col("sentiment") == "positive").count()
neg_no=df.filter(col("sentiment") == "negative").count()
print("Positive:",pos_no)
print("Negative:",neg_no)

# 5. Transform
df = df.withColumn("review_length", length(col("review")))
long_rev=df.filter(col("review_length") > 500)
long_rev.show(10)
print("Reviews longer than 500 charachters = ", long_rev.count())
# 6. Save
df.write.mode("overwrite").option("header", True).option("quote", '"').option("escape", '"').csv("imdb_output")

spark.stop()