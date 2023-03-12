from django.urls import path

from api.views import ProductAPIView

app_name = "api"

urlpatterns = [
    path("", ProductAPIView.as_view(), name="products"),
]