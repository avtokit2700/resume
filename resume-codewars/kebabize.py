#Test.assert_equals(kebabize('myCamelCasedString'), 'my-camel-cased-string')
#Test.assert_equals(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
#Test.assert_equals(kebabize('SOS'), 's-o-s')
#Test.assert_equals(kebabize('42'), '')
#Test.assert_equals(kebabize('CodeWars'), 'code-wars')


def kebabize(string):
    result = ''
    for t in string:
        if t.islower():
            result += t
        elif t.isupper():
            result += '-'+ t.lower()
        elif t.isnumeric():
            result += ''
    if string.isnumeric():
        return ''
    if result[0] == '-':
        return result[1:]
    return result

print(kebabize('myCamelHas3Humps'))