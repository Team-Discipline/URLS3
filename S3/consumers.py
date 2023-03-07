import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from S3.models import S3


class AdPageConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        if self.scope.get('url_route', None) and self.scope['url_route'].get('kwargs', None):
            hashed_value = self.scope["url_route"]["kwargs"]['hashed_value']

            try:
                # When only protocol is fit and hash value is valid.
                s3 = await S3.objects.aget(hashed_value__hash_value=hashed_value)
                await self.accept()
                await asyncio.sleep(3)
                return await self.send_json({'success': True,
                                             'msg': 'go to target_url!',
                                             'target_url': s3.target_url},
                                            close=True)
            except S3.DoesNotExist:
                await self.send_json({
                    'success': False,
                    'msg': '해당되는 S3 데이터를 찾을 수 없습니다.'
                }, close=True)
        else:
            await self.send_json({
                'success': False,
                'msg': '해시값이 필요합니다.'
            }, close=True)

    async def wait_for_ads(self, second: int = 5):
        return await asyncio.sleep(second)
