from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response

from user_profile.models import UserProfile, Image
from user_profile.serializers import UserProfileSerializer, ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]
    http_method_names = ['post', 'get', 'put', 'delete']

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']
    lookup_field = 'user_id'

    def create(self, request: Request, *args, **kwargs):
        """
        먼저 `POST /profile/image/`에서 이미지 url을 생성하고
        그 다음에 그 url을 `thumbnail_url`에 넣어서 request해주세요.
        """
        user = self.request.user
        print(f'requested user: {user}')
        url = request.data.get('thumbnail_url')
        print(f'url: {url}')

        profile = UserProfile(user_id=user.pk, thumbnail=url)
        profile.save()

        s = UserProfileSerializer(profile)

        return Response(s.data)
