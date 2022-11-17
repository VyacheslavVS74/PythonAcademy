s = "Замените в этой строке все появления буквы 'о' на букву 'О', кроме первого и последнего вхождения"
# s = input('-> ')
# print(s)

s = s.replace('о', 'О', s.count('о') - 1)
s = s.replace('О', 'о', 1)
print(s)

# a = s[:s.find('о') + 1]
# # print(a)
# b = s[s.find('о') + 1:s.rfind('о')]
# c = s[s.rfind('о'):]
# s = a + b.replace('о', 'О') + c
# print(s)

