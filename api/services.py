import openpyxl
import requests


def get_product_data(article):
    url = f'https://basket-05.wb.ru/vol735/part73512/{article}/info/ru/card.json'
    response = requests.get(url)
    data = response.json()
    brand = data.get('selling').get("brand_name")
    article_title = data.get('subj_name')
    return brand, article_title


def get_articles_from_xlsx(file):
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook.active
    articles = [row[0] for row in worksheet.iter_rows(values_only=True)]
    return articles