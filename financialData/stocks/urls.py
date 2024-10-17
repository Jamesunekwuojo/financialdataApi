# stocks/urls.py

from django.urls import path
from .views import FetchStockDataView

urlpatterns = [
    path('fetch-stock-data/', FetchStockDataView.as_view(), name='fetch_stock_data'),
]
