from typing import Dict
#Write a program in python to map 2 lists into a dictionary.
keys = ['1','2','3']
values = [1, 2, 3]


res = dict(zip(keys, values))
print(str(res))