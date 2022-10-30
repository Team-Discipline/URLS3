from django.apps import AppConfig


class S3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'S3'

    def ready(self):
        """
        `utils.words_excel`안에 있는 엑셀 파일을 불러들여 `Word` 모델에 저장합니다.
        주석 건들지 마시오.
        """
        # from .utils.LoadWords import load_adj, load_noun, delete_every_words
        # delete_every_words()
        # load_adj()
        # load_noun()
        ...
