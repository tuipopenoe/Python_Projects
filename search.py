from SOAPpy import WSDL
from PrivateKeys import googlesearch, googleapikey

WSDFILE = googlesearch.url
APIKEY = googleapikey.apikey

_server = WSDL.Proxy(WSDLFILE)

def search(q):
    """Search Google and return list of (title, link, description)"""
    results = _server.doGoogleSearch(
        APIKEY, q, 0, 10, False, "", False, "", "utf-8", "utf-8")
    return [{"title": r.title.encode("utf-8"),
        "description": r.snippet.encode("utf-8")}
        for r in results.resultElements]

if __name__ == '__main__':
    import sys
    for r in search(sys.argv[1])[:5]:
        print r['title']
        print r['link']
        print r['description']
        print