import re

def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman_num = ''
    for i in range(len(val)):
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
    return roman_num

def roman_to_int(s):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and val[s[i]] < val[s[i + 1]]:
            total -= val[s[i]]
        else:
            total += val[s[i]]
    return total

replacements = []
