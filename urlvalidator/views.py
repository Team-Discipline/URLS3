from rest_framework import viewsets
from rest_framework.decorators import api_view
from urlvalidator.serializers import URLSerializer
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from urllib.parse import urlparse


@api_view(["POST"])
def is_valid_url(request):
    serializer = URLSerializer(data=request.data)
    validator = URLValidator(verify_exists=True)
    # url = models.URLField(verify_exists=True)
    protocol = urlparse(request).scheme
    schemes_list = ['http', 'https', 'ftp', 'ftps', 'mailto', 'news', 'irc', 'gopher', 'nntp', 'feed', 'telnet', 'mms',
                    'rtsp', 'svn', 'tel', 'fax', 'xmpp']

    if request.startswith("http"):
        print(f'url {request} start with any secure protocols.')
        # 받은 url이 https 프로토콜이 아니라면 경고를 보내줍니다.
    if protocol not in schemes_list:
        print(ValidationError)
    try:
        validator(request)
        # url is valid here
        # url is valid 인 상태이므로 다음으로 넘겨주면 됩니다
        serializer.save()
        return True

    except ValidationError:
        print(ValidationError)
        print(f'This url: {request} is not valid. Try another')
        return False
