# title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
# title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
import re


def title_case(title, minor_words):
    cont = title.split()[0].title() + ' '
    minor_words = minor_words.lower()
    if minor_words:
        title = title.lower().title()
        for word in title.split()[1:]:
            if len(word) <= 3:
                cont += word.lower() + ' '
            else:
                cont += word + ' '
        return cont
    else:
        return title.title()


print(title_case('THE WIND IN THE WILLOWS', 'The In'))