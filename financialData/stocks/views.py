from django.shortcuts import render

# Create your views here.
# stocks/views.py

from django.http import JsonResponse
from django.views import View
from .services import fetch_stock_data

class FetchStockDataView(View):
    """
    View to trigger fetching stock data for a given symbol.
    """
    def get(self, request, *args, **kwargs):
        symbol = request.GET.get('symbol', 'AAPL')  # Default to AAPL if no symbol provided
        try:
            result = fetch_stock_data(symbol)
            return JsonResponse({'message': result}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
