from mapreduce import shuffle

mapped_data = [

('HTTP_404',1),
('Hour_14',1),
('HTTP_500',1),
('Hour_14',1)

]

result = shuffle(mapped_data)

print(dict(result))