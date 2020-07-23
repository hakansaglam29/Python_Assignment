sentence = input("Please enter a sentence: ")
s_dict = {}
for i in sentence:
    s_dict.update({i:sentence.count(i)})
print(s_dict)