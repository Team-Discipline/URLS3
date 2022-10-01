import requests

from S3.models import S3SecurityResult, S3


class URLSecurityChecker:
    """
    The class that check given url address' security.
    """

    def __init__(self, s3_url, url_address):
        has_hsts = self._has_hsts(url_address)

        s3 = S3.objects.get(s3_url=s3_url)
        self.result = S3SecurityResult(s3=s3, has_hsts=has_hsts)

        self.result.save()

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
