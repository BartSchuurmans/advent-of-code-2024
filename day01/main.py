import polars as pl
from pathlib import Path


df = pl.read_csv(
    Path(__file__).parent / "input.txt",
    has_header=False,
    separator=" ",
).select(left=pl.col("column_1"), right=pl.col("column_4"))

total_distance = df.select(
    (pl.col("left").sort() - pl.col("right").sort()).abs().sum()
).item()
print(f"Day 01, part 1: total distance is {total_distance}")
