import requests

from S3.models import S3SecurityResult


class URLSecurityChecker:
    """
    The class that check given url address' security.
    """

    @staticmethod
    def _has_hsts(site) -> bool:
        try:
            res = requests.get(site)
        except requests.exceptions.SSLError:
            return False
        except requests.exceptions.MissingSchema:
            site = 'https://' + site
            res = requests.get(site)

        if 'strict-transport-security' in res.headers:
            return True
        else:
            return False

    @staticmethod
    def check(url_address) -> S3SecurityResult:
        has_hsts = URLSecurityChecker._has_hsts(url_address)
        result = S3SecurityResult(has_hsts=has_hsts)
        result.save()
        return result
