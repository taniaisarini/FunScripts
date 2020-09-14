def anagram(s):
    if len(s) == 1:
        return [s]
    else:
        list1 = anagram(s[1:])
        list2 = []
        letter = s[0]
        s = s[1:]
        for word in list1:
            for i in range(0, len(word) + 1):
                new_word = s[:i] + letter + s[i:]
                list2.append(new_word)
        return list2


print(anagram("abc"))
