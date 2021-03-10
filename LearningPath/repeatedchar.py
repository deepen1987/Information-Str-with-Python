# Find the most repeated character in the text
import pprint as pp

sentence = "This is a common interview question"
# Create a list from sentence
listChar = set([str for str in sentence if str != ' '])
char = ""
charCount1 = 0
for item in listChar:
    Count = sentence.count(item)
    if Count > charCount1:
        charCount1 = Count
        char = item
print(f"{char} is most repeated {charCount1}")

char_frequency = {}
for item in sentence:
    if item in char_frequency:
        char_frequency[item] += 1
    else:
        char_frequency[item] = 1
char_frequency = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)
pp.pprint(char_frequency[0])
