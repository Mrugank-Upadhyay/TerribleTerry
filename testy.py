def getBio(handle):
    import urllib
    import requests
    url = "https://twitter.com/" + handle
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    return (mystr[4690:4990])


