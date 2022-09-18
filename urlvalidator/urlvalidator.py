# from django.core.validators import URLValidator
# from django.core.exceptions import ValidationError
# from urllib.parse import urlparse
# from django.db import models
#
#
# def url_validator(input_url: str):
#     validator = URLValidator(verify_exists=True)
#     url = models.URLField(verify_exists=True)
#     split_url = urlparse(input_url)
#     schemes_list = ['http', 'file', 'ftp', 'gopher', 'hdl', 'http', 'https', 'imap', 'mailto', 'mms', 'news', 'nntp',
#                     'prospero', 'rsync',
#                     'rtsp', 'rtspu', 'sftp', 'shttp', 'sip', 'sips', 'snews', 'svn', 'svn+ssh', 'telnet', 'wais', 'ws',
#                     'wss']
#     # urls3에서 받은 url을 input_url로 받으면 됩니다.
#     for i in range(len(schemes_list)):
#         if split_url.scheme in schemes_list[i] is False:
#             print(f'url {input_url} start with any protocols.')
#
#     if (split_url.scheme == 'https') is False:
#         print(f'This {split_url.scheme} has no secure. Are you sure to get S3?')
#     # 받은 url이 https 프로토콜이 아니라면 경고를 보내줍니다.
#     try:
#         validator(input_url)
#         # url is valid here
#         # url is valid 인 상태이므로 다음으로 넘겨주면 됩니다. (다음이란건 urls3 생성)
#         return True
#     except ValidationError as exception:
#         # URL is NOT valid here.
#         # exception or error code 를 넣으면 됩니다.
#         print(exception)
#         print(f'This url: {input_url} is not valid. Try another')
#         return False
