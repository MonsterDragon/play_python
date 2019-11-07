#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from collections import Counter

words = ["aa", "bb", "cc", "dd", "aa", "cc", "aa", "bb", "ee"]
word_counts = Counter(words)
print(word_counts)
print(type(word_counts))
top_three = word_counts.most_common(3)
print(top_three)
more_words = ["cc", "cc", "bb"]
# for word in more_words:
#     word_counts[word] += 1
word_counts.update(more_words)
print(word_counts.most_common(3))

a = Counter(words)
b = Counter(more_words)

print(a)
print(b)

print("a+b: ", a+b)
print("b-a: ", a-b)
