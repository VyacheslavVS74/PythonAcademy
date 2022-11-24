import re

# 1)----------------------------------------------------------------------

st = '1X Text ABC 123 A1B2C3'
# =========
reg = r'\D(\d)'
# reg = r'[^\d](\d)'
print(re.findall(reg, st))
# =========
# reg = r'(?<!\d)(\d)(?!\d)'
# print(re.findall(reg, st))

# 2) ----------------------------------------------------------------------

st1 = 'text from #START# till #END#'
# =========
# reg = r'([#\w+#])(\s\w+\s)\1'
# print(re.search(reg, st1).group(2))
# =========
# reg = r'(?<=#START#).*?(?=#END#)'
# print(re.findall(reg, st1))

# 3) ----------------------------------------------------------------------

# st3 = '12_34__56'
# reg = r'\d+(?=_\d)'
# print(re.findall(reg, st3))

