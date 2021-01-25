import re
from urllib.parse import urlparse

def extract_doi(inputstring):
    url = extract_url_from_string(inputstring)

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

def extract_url_from_string(inputstring):
    try:
        result = re.search("(?P<url>https?://[^\s]+)", inputstring).group("url").replace('\"', '')
    except Exception as e:
        result = "NOT FOUND" + str(e)

    return result