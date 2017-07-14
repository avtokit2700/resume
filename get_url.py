# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"
import re
def domain_name(url):
    if re.search('www', url):
        return str(re.findall('\..+\.', url))[3:-3]
    elif re.search('http:', url) or re.search('https:', url):
        return str(re.findall('//.+\.', url))[4:-3]

def domain_name_best(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

print(domain_name("https://www.cnet.com"))
print(domain_name_best("https://www.cnet.com"))