from pyspark.sql import SparkSession


def main() -> None:
    spark = SparkSession.builder.getOrCreate()
    print(f"ExplorAI smoke test passed. Spark version: {spark.version}")


if __name__ == "__main__":
    main()
