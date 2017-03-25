"""

    Removes any duplicate query string parameters from the url
    Removes any query string parameters specified within the 2nd argument (optional array)

Examples:

stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'

"""
a = 'www.codewars.com?a=1&b=2&a=2'
b = 'www.codewars.com'
import re

def strip_url_params(url, params_to_strip = []):
    adr_part = re.split(r'\?', url)[0]
    if '?' in url and params_to_strip:
        razd = '&' + params_to_strip[0]
        return url.split(razd)[0]
    if '?' in url:
        query_part = re.split(r'\?', url)[1]
        res = ''
        lst = query_part.split('&')
        for l in lst:
            if l[0] not in res:
                res += str(l) + '&'
        return adr_part + '?' + res[:-1]
    return url

print(strip_url_params(a))