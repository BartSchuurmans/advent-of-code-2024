from pathlib import Path

with open(Path(__file__).parent / "input.txt") as f:
    xys = [line.split() for line in f]
    xs = sorted(int(xy[0]) for xy in xys)
    ys = sorted(int(xy[1]) for xy in xys)

total_distance = sum(abs(x - y) for x, y in zip(xs, ys))
print(f"Day 01, part 1: total distance is {total_distance}")

similarity_score = sum(x * ys.count(x) for x in xs)
print(f"Day 01, part 2: similarity score is {similarity_score}")
