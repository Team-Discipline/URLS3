from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class ValidationCheck:

    def valid_url(self) -> bool:
        validator = URLValidator()
        # urls3에서 받은 url을 to_validate로 받으면 됩니다.
        if self.startswith("http"):
            print(f'url {self} start with no security.')
            # 받은 url이 https 프로토콜이 아니라면 경고를 보내줍니다.
        try:
            validator(self)
            # url is valid here
            # url is valid 인 상태이므로 다음으로 넘겨주면 됩니다. 다음이란건 urls3 생성
            return True
        except ValidationError as exception:
            # URL is NOT valid here.
            # exception or error code 를 넣으면 됩니다.
            print(exception)
            return False
