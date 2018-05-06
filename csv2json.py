#!/opt/spark/bin/spark-submit

from pyspark.sql import SparkSession
from pyspark.sql.types import *

# data from https://www.kaggle.com/nickhould/craft-cans
beers_csv = 'file:///srv/beers.csv'
breweries_csv = 'file:///srv/breweries.csv'
export_json = 'file:///srv/export_json'

app_name = 'csv2json'

spark = SparkSession.builder.appName(app_name).getOrCreate()

#
# beers
#
beers_schema = StructType(
    [
        StructField('_c0', IntegerType(), False),
        StructField('abv', DoubleType(), True),
        StructField('ibu', DoubleType(), True),
        StructField('id', IntegerType(), False),
        StructField('name', StringType(), False),
        StructField('style', StringType(), True),
        StructField('brewery_id', IntegerType(), False),
        StructField('ounces', DoubleType(), True),
    ]
)

beers_df = spark.read.csv(beers_csv, header=True, schema=beers_schema)
beers_df.registerTempTable('beers_table')

# beers_df = beers_df1.union(beers_df2)

#
# breweries
#
breweries_schema = StructType(
    [
        StructField('id', IntegerType(), False),
        StructField('name', StringType(), False),
        StructField('city', StringType(), True),
        StructField('state', StringType(), True),
    ]
)

breweries_df = spark.read.csv(breweries_csv, header=True, schema=breweries_schema)
breweries_df.registerTempTable('breweries_table')

# join
sql = 'select p.id, p.name, p.style, p.abv, p.ibu, p.ounces, p.brewery_id, q.name as brewery_name, q.city, q.state from beers_table as p inner join breweries_table as q on p.brewery_id = q.id'

joined = spark.sql(sql)
joined.write.json(export_json)
