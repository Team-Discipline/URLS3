from django.apps import AppConfig


class S3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'S3'

    def ready(self):
        from . import signals
        """
        밑의 줄을 import 함으로써 `utils.words_excel`안에 있는 엑셀 파일을 불러들여
        `Word` 모델에 저장합니다.

        평상시에는 주석을 해제하지 마십시오.
        """

        # from .utils import LoadWords
        ...
