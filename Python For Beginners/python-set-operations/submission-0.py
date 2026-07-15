from typing import List

def count_unique_words(words: List[str]) -> int:
 my_set=set()
 for word in words:
     my_set.add(word)
 return len(my_set)


# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
