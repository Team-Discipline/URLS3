from urlvalidator.serializers import URLSerializer
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from urlvalidator.models import models


# docs/url/s3 get
def is_valid_url(input_url) -> bool:
    # queryset = models.URLField.objects.all()
    # serializer = URLSerializer(data=input_url.data)
    validator = URLValidator(verify_exists=True)
    url = models.URLField(verify_exists=True)

    try:
        if input_url.startswith("http" or "ftps"):
            print(f'url {input_url} start with no secure protocols.')
        validator(input_url)
        # 받은 URL이 secure이 포함된 프로토콜이 아니라면 경고를 보내줍니다.
        # url is valid here
        # url is valid 인 상태이므로 다음으로 넘겨주면 됩니다
        # serializer.save()
        return True

    except ValidationError:
        print(ValidationError)
        print(f'This url: {input_url} is not valid. Try another')
        return False
