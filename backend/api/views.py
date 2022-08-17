from django.shortcuts import render, redirect
from django.db import connection
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer
import datetime,json
import requests
from bs4 import BeautifulSoup

class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

@api_view(['GET'])
def get_stock(request):
    if request.method == 'GET':        
        stocks = Stock.objects.all().order_by("name")
        stock_serializer = StockSerializer(stocks, context={'request': request}, many=True)
        return Response(stock_serializer.data, status=200)

@api_view(['GET'])
def check_stock(request):
    if request.method == 'GET':
        url = "https://www.investing.com/equities/StocksFilter?noconstruct=1&smlID=0&sid=&tabletype=price&index_id=20"
        header = {
            'Host': 'www.investing.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive'
        }
        # stock = []
        
        Stock.objects.all().delete()

        openUrl = 'https://www.investing.com'
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        tableInfo = soup.find_all("tr")
        for trIndex, trInfo in enumerate(tableInfo): 
            if trIndex == 0: continue
            tdInfos = trInfo.find_all("td")
            
            item = {}
            stock = Stock()
            for tdIndex, tdContent in enumerate(tdInfos):
                if (tdIndex == 0): continue
                if (tdIndex == 1):
                    stock.name = tdContent.text

                    a = tdContent.find("a").get("href")
                    href = openUrl + a
                    symbolHtml = requests.get(href, headers=header)
                    content = BeautifulSoup(symbolHtml.text, "html.parser")
                    title = content.find("meta",  itemprop="tickerSymbol")

                    stock.symbol = title["content"]
                if (tdIndex == 2):
                    stock.last_price = tdContent.text
                if (tdIndex == 6):
                    stock.changed_value = tdContent.text
                if (tdIndex == 7):
                    stock.volume = tdContent.text
            
            stock.save()
        return redirect(get_stock)
