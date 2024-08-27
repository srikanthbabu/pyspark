# Databricks notebook source
df = spark.read \
    .format("csv")\
    .option("header","true") \
    .option("inferschema","true")\
    .load("/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-calls.csv")


# COMMAND ----------

df.show(10)

# COMMAND ----------

display(df)

# COMMAND ----------

df.createGlobalTempView("tableFire")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from global_temp.tablefire

# COMMAND ----------



# COMMAND ----------


