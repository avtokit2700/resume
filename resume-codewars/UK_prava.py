mon = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
       'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09',
       'Oct': '10', 'Nov': '11', 'Dec': '12'}

def driver(data):
    if len(data[2]) > 4:
        name = data[2].upper()[:5]
    else:
        name = (data[2].upper() + '999')[:5]
    year_of_1 = data[3][-2]
    if data[-1] == 'M':
        month = mon.get(data[3][3:6])
    else:
        month = int(mon.get(data[3][3:6])) + 50
    day = data[3][:2]
    year_of_2 = data[3][-1]
    if data[1]:
        lit_name = data[0][0] + data[1][0]

    else:
        lit_name = data[0][0] + '9'

    return '{}{}{}{}{}{}'.format(name, year_of_1, month, day, year_of_2, lit_name) + '9AA'

print(driver(["John", "James", "Smith", "01-Jan-2000", "M"]))
if driver(["Andrew", "Robert", "Lee", "02-September-1981", "M"]) == "LEE99809021AR9AA":
    print("Kurwa GOOD")

# "SMITH001010JJ9AA"
