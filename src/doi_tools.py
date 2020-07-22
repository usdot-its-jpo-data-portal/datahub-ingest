import re
from urllib.parse import urlparse

def extractDOI(inputstring):
    url = extractURLFromString(inputstring)

    if (url != 'NOT FOUND'): # Valid URL found in string
        urltuple = urlparse(url)
        if (urltuple.netloc != 'doi.org'): # URL is valid, but isn't from DOI
            result = 'INVALID'
        else: # valid DOI URL
            result = url

    else: #No valid URL found in string
        result = "INVALID"

    print(result)

    return result

def extractURLFromString(inputstring):
    try:
        result = re.search("(?P<url>https?://[^\s]+)", inputstring).group("url").replace('\"', '')
    except:
        result = "NOT FOUND"
    return result