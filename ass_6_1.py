def string_reverse(str1):

    astr1 = ''
    index = len(str1)
    while index > 0:
        astr1 += str1[ index - 1 ]
        index = index - 1
    return astr1
print(string_reverse('sayani'))