import aiohttp
import openpyxl
from rest_framework.response import Response
from rest_framework.views import APIView

from api.pydantic import ProductData


class ProductAPIView(APIView):

    async def get_product_data(self, article):
        url = f'https://basket-05.wb.ru/vol735/part73512/{article}/info/ru/card.json'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                brand = data.get('selling').get("brand_name")
                article_title = data.get('subj_name')
        return brand, article_title

    async def post(self, request):
        file = request.data.get('file')
        article = request.data.get('article')

        if file:
            workbook = openpyxl.load_workbook(file)
            worksheet = workbook.active
            articles = [row[0] for row in worksheet.iter_rows(values_only=True)]

        elif article:
            articles = [article]

        else:
            return Response({'error': 'Необходимо передать файл или одно значение артикула'})

        products_data = []
        for article in articles:
            brand, article_title = await self.get_product_data(article)
            product_data = ProductData(article=article, article_title=article_title, brand=brand)
            products_data.append(product_data.dict())

        return Response(products_data)
