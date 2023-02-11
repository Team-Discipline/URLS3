from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response

from user_profile.models import UserProfile, Image
from user_profile.serializers import UserProfileSerializer, ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    이미지 수정을 원하면 계속 `POST`하면 됩니다.
    기존 이미지는 삭제 됩니다.
    `PATCH /profile/{user_id}/`로 프로필을 업데이트 하지 않으면,
    `GET /profile/`, `GET /profile/{user_id}/`에 사진이 뜨지 않습니다.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]
    http_method_names = ['post', 'get', 'delete']

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            image = Image.objects.get(uploaded_by=self.request.user)
            image.delete()
        except Image.DoesNotExist:
            ...
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        image = list(get_list_or_404(Image, uploaded_by=self.request.user))
        images = image
        image = images.pop()
        if len(images) > 0:
            for i in images:
                i: Image
                i.delete()

        s: ImageSerializer = self.get_serializer(image)
        return Response(s.data)


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    `POST /profile/image/`에 업로드하면 알아서 `thumbnail` field가 채워집니다.
    하지만 반드시 `POST /profile/`을 불러야 프로필이 생성이 됩니다.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'user_id'

    def create(self, request: Request, *args, **kwargs):
        # Find image uploaded by user.
        # If not found anything, Just put `None` to `UserProfile`.
        try:
            image = Image.objects.get(uploaded_by=self.request.user)
        except Image.DoesNotExist:
            image = None
            ...

        # If already user's profile exists, Delete it.
        try:
            p = UserProfile.objects.get(user=self.request.user)
            p.delete()
        except UserProfile.DoesNotExist:
            ...

        profile = UserProfile(user=self.request.user, thumbnail=image)
        profile.save()
        s = UserProfileSerializer(profile, context={'request': request})
        return Response(s.data)

    def list(self, request, *args, **kwargs):
        try:
            profile = self.get_queryset().get(user=self.request.user)
            print(f'{profile=}')
            s = UserProfileSerializer(profile, context={'request': request})
            return Response(s.data)
        except UserProfile.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='Not found that user.')

    def retrieve(self, request, *args, **kwargs):
        """
        **사용 금지**
        """
        return Response(status=status.HTTP_404_NOT_FOUND)
