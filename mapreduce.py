import re
from collections import defaultdict

# ---- SPLIT ----
def split_file(filepath, num_chunks=4):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    chunk_size = max(1, len(lines) // num_chunks)
    return [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]

# ---- MAP ----
def map_chunk(chunk):
    results = []
    for line in chunk:
        status = re.search(r'" (\d{3}) ', line)
        hour = re.search(r':(\d{2}):\d{2}:\d{2}', line)
        if status:
            results.append((f"HTTP_{status.group(1)}", 1))
        if hour:
            results.append((f"Hour_{hour.group(1)}", 1))
    return results

# ---- SHUFFLE ----
def shuffle(mapped_results):
    shuffled = defaultdict(list)
    for pairs in mapped_results:
        for key, val in pairs:
            shuffled[key].append(val)
    return shuffled

# ---- REDUCE ----
def reduce_group(key_values):
    key, values = key_values
    return (key, sum(values))

# ---- FULL PIPELINE ----
def run_mapreduce(filepath):
    chunks = split_file(filepath)
    # Map phase (sequential for cloud compatibility)
    mapped = [map_chunk(chunk) for chunk in chunks]
    # Shuffle phase
    shuffled = shuffle(mapped)
    # Reduce phase
    reduced = [reduce_group(item) for item in shuffled.items()]
    return dict(reduced)