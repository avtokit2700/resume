# Test.assert_equals(is_valid_IP('12.255.56.1'),     True)
# Test.assert_equals(is_valid_IP(''),                False)
# Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
# Test.assert_equals(is_valid_IP('123.456.789.0'),   False)
# Test.assert_equals(is_valid_IP('12.34.56'),        False)
# Test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
# Test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
# Test.assert_equals(is_valid_IP('123.045.067.089'), False)
import re


def is_valid_IP(strng):
    Ip = re.split(r'\.', strng)
    flag = 0
    if ''.join(Ip).isdigit():
        for i in Ip:
            if 256 > int(i) > 0 and int(i[0]) != 0 and len(Ip) == 4:
                flag += 1
            else:
                return False
    else:
        return False
    if flag == 4:
        return True



print(is_valid_IP('12.255.56.1'))