"""
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
"""
a = "apples, pears # and bananas\ngrapes\nbananas !apples"
b = "a #b\nc\nd $e f g"
import re


def solution(string, markers):
    # Находим шаблон для разделению split
    markers = r'|'.join(re.escape(marker) for marker in markers)
    # Берем строку, сравниваем, есть ли в ней символ из markers, и разделяем по этому символу, запись первой части
    words = [re.split(markers, word)[0].rstrip() for word in string.split('\n')]
    return '\n'.join(words)

print(solution(a, ["#", "!", '@', '$']))