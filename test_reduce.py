from mapreduce import reduce_data

grouped_data = {

    'HTTP_404': [1, 1, 1],
    'HTTP_500': [1, 1],
    'Hour_14': [1, 1, 1, 1]

}

result = reduce_data(grouped_data)

print(result)