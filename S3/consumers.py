import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from S3.models import Hash, S3
from analytics.models import CapturedData
from analytics.serializers import GetCapturedDataSerializer


class AdPageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        if self.scope.get('url_route', None) and self.scope['url_route'].get('kwargs', None):
            hashed_value = self.scope["url_route"]["kwargs"]['hashed_value']

            try:
                # When only protocol is fit and hash value is valid.
                await Hash.objects.aget(hash_value=hashed_value)
                return await self.accept()
            except Hash.DoesNotExist:
                return
        else:
            return

    async def receive_json(self, content, **kwargs):
        if content.get('captured_data', None):
            captured_data_id = content['captured_data']
            try:
                c = await CapturedData.objects.aget(id=captured_data_id)
                s = GetCapturedDataSerializer(c)
                await self.send_json({'message': 'data checked', 'content': s.data})
                await self.wait_for_ads()
                s3 = await S3.objects.aget(id=s.data.get('s3'))
                return await self.send_json({'success': True,
                                             'message': 'go to target_url!',
                                             'target_url': s3.target_url},
                                            close=True)
            except CapturedData.DoesNotExist:
                return await self.send_json({'success': False, 'message': 'cannot find data.'})

    async def wait_for_ads(self, second: int = 5):
        return await asyncio.sleep(second)
