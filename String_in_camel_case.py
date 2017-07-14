"""
# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior")

# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")
to_camel_case("A-B-C"), "ABC"
"""
import re


def to_camel_case(text):
    result = ''
    final = ''
    if text:
        for t in text:
            if t.isalpha():
                result += t
            elif t == '-' or t == '_':
                result += ' '
        for word in result.split():
            final += word.title()
        if text[0].islower():
            final = final[0].lower() + final[1:]
    return final

print(to_camel_case("The_Stealth_Warrior"))
