from hashtable import Hashtable


def most_common_word(string):
    ht = Hashtable(1024)
    list_of_strings = string.split(" ")
    current_highest = ("", 0)
    for strng in list_of_strings:
        if ht.contains(strng):
            current_count = ht.get(strng) + 1
            ht.update(strng, current_count)
            if current_highest[1] < current_count:
                current_highest = (strng, current_count)
        else:
            ht.add(strng, 1)
    return current_highest[0]
