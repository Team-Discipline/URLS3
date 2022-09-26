from rest_framework import viewsets
from urlvalidator.serializers import URLSerializer
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from urlvalidator.models import URLModel


# docs/url/s3 get
class ValidateUrl(viewsets.ModelViewSet):
    url = URLModel

    def is_valid_url(self, url) -> bool:
        validator = URLValidator(verify_exists=True)
        try:
            if url.startswith("http" or "ftps"):
                print(f'url {url} start with no secure protocols.')
            validator(url)
            # 받은 URL이 secure이 포함된 프로토콜이 아니라면 경고를 보내줍니다.
            # url is valid here
            # url is valid 인 상태이므로 다음으로 넘겨주면 됩니다
            # serializer.save()
            return True

        except ValidationError:
            print(ValidationError)
            print(f'This url: {url} is not valid. Try another')
            return False
