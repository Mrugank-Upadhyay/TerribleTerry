def getBio(handle):
    import urllib
    import requests
    url = "https://twitter.com/" + handle
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    bioStart = 4690
    bioEnd = 4990
    return (mystr[bioStart : bioEnd])


