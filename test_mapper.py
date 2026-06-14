from mapreduce import mapper

sample_chunk = [

'127.0.0.1 - - [10/May/2025:14:05:12] "GET /about.html HTTP/1.1" 404',

'127.0.0.1 - - [10/May/2025:14:07:15] "POST /login HTTP/1.1" 500'

]

result = mapper(sample_chunk)

print(result)