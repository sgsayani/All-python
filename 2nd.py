Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> range(10_
      
SyntaxError: invalid decimal literal
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(range(10))
<class 'range'>
>>> range(50)
range(0, 50)
>>> list(range(50))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> B=100
>>> l=800
>>> B<l
True
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(B<l)
<class 'bool'>
>>> str = "Hello World")
SyntaxError: unmatched ')'
>>> str = "Hello World"
>>> type(str)
<class 'str'>
>>> len(str)
11
>>> d = {'Sayani':'Samsung','Hrithik':'redmi','Sourashish':'One plus'}
>>> d.keys()
dict_keys(['Sayani', 'Hrithik', 'Sourashish'])
>>> d.values()
dict_values(['Samsung', 'redmi', 'One plus'])
>>> 