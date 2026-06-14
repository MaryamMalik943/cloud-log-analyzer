from mapreduce import split_data

data = [
    "line1",
    "line2",
    "line3",
    "line4",
    "line5",
    "line6"
]

chunks = split_data(data, 2)

print(chunks)