from collections import Counter
def caracteres(string_1, string_2):
    counter_1 = Counter(string_1)
    counter_2 = Counter(string_2)
    common = counter_1 & counter_2
    if len(common)==0:
        return 
    common = list(common.elements())
    common = ''.join(common)
    return common
    
word_1 = str(input("Type your first word: "))
word_2 = str(input("Type your second word: "))

print(f"Your similiars words is: {caracteres(word_1,word_2)}")