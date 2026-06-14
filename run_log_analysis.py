from mapreduce import split_data, mapper, shuffle, reduce_data

# Read log file

with open("uploads/sample_log.log", "r") as file:
    lines = file.readlines()

# Split

chunks = split_data(lines, 5)

# Map

mapped_results = []

for chunk in chunks:
    mapped_results.extend(mapper(chunk))

# Shuffle

grouped = shuffle(mapped_results)

# Reduce

final_result = reduce_data(grouped)

print(final_result)