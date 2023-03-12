from rest_framework.response import Response
from rest_framework.views import APIView

from api.pydantic import ProductData
from api.services import get_product_data, get_articles_from_xlsx


class ProductAPIView(APIView):

    def post(self, request):
        file = request.data.get('file')
        article = request.data.get('article')

        if file:
            articles = get_articles_from_xlsx(file)

        elif article:
            articles = [article]
        else:
            return Response({'error': 'Необходимо передать файл или одно значение артикула'})

        products_data = []
        for article in articles:
            brand, article_title = get_product_data(article)
            product_data = ProductData(article=article, article_title=article_title, brand=brand)
            products_data.append(product_data.dict())

        return Response(products_data)