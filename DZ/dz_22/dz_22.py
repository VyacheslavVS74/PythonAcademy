import re

# s1 = '+7 499 256-45-78, +74994566478, 7 (499) 456 45 78, 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s1))
s1 = """

+74994564578
7 (499) 456 45 78
7 (499) 456-45-78
"""

s = '+7 499 456-45-78'
reg = r'^(+7[\- ]?)([\(]?\d{3}[\)]?[ \-]?)?[\d\- ]{7,10}$'


print(re.findall(reg, s))

# print(re.findall(reg, s1))
# print(re.findall(reg, s2))
# print(re.findall(reg, s3))


# ^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$

# t = "2324 786 22 4569"
# # reg = r'\d{1,3}'  # жадное регулярное выражение
# reg = r'\d{1,3}?'  # ленивое регулярное выражение
# print(re.findall(reg, t))