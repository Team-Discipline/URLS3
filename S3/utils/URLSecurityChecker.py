import requests

from S3.models import S3SecurityResult


class URLSecurityChecker:
    """
    The class that check given url address' security.
    """

    def __init__(self, url_address):
        has_hsts = self._has_hsts(url_address)

        self.result = S3SecurityResult(has_hsts=has_hsts)

    def _has_hsts(self, site) -> bool:
        try:
            req = requests.get(site)
        except requests.exceptions.SSLError:
            return False
        except requests.exceptions.MissingSchema:
            site = 'https://' + site
            req = requests.get(site)

        if 'strict-transport-security' in req.headers:
            return True
        else:
            return False
