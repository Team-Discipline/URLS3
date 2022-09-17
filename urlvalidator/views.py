from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


# Create your views here.
class URLValidationViewSet:
    http_method_names = ['post', 'get', 'delete']

    def __init__(self):
        self.POST = None
        self.method = None

    def url_validator(self):
        if self.method == "POST":
            valid_url = self.POST["textfield"]
            validator = URLValidator()
            # urls3에서 받은 url을 to_validate로 받으면 됩니다.
            if valid_url.startswith("http"):
                print(f'url {valid_url} start with no security.')
                # 받은 url이 https 프로토콜이 아니라면 경고를 보내줍니다.
            try:
                validator(valid_url)
                # url is valid here
                # url is valid 인 상태이므로 다음으로 넘겨주면 됩니다. 다음이란건 urls3 생성
                return True
            except ValidationError as exception:
                # URL is NOT valid here.
                # exception or error code 를 넣으면 됩니다.
                print(exception)
                print(f'This url: {valid_url} is not valid. Try another')
                return False

