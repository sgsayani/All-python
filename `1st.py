Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> a
10
>>> PI = 3.14
>>> type(PI)
<class 'float'>
>>> type(a)
<class 'int'>
>>> num = 3+4j
>>> type(num)
<class 'complex'>
>>> a=5.9
>>> b=52
>>> type(b)
<class 'int'>
>>> b=int(a)
>>> type(b)
<class 'int'>
>>> b=float(a)
>>> type(b)
<class 'float'>
>>> b
5.9
>>> k=float(b)
>>> k
5.9
>>> c= complex(b,k)
>>> c
(5.9+5.9j)
>>> c = complex(a,b)
>>> c
(5.9+5.9j)
>>> a
5.9
>>> b=52
>>> b
52
>>> c = complex(a,b)
>>> c
(5.9+52j)
>>> b>k
True
>>> b<k
False
>>> bool = b<k
>>> bool
False
>>> type(b<k)
<class 'bool'>
>>> int(True)
1
>>> int(False)
0
>>> sg = {54, 45, 87, 45}
>>> type(sg)
<class 'set'>
>>> t=[21,01,32,45]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> t=[78, 54, 45, 8]
>>> type(t)
<class 'list'>
>>> str="Sayani"
>>> type(str)
<class 'str'>
>>> tp=(54, 87,100)
>>> type(tp)
<class 'tuple'>
>>> 