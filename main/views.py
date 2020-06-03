from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import django
django.setup()
from .models import Currency, Price

import requests
import json
from multiprocessing import Pool
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.

api_url = "https://query1.finance.yahoo.com/v8/finance/chart/{}?region=GB&lang=en-GB&includePrePost=false&interval={}&range={}&corsDomain=uk.finance.yahoo.com&.tsrc=finance"

def home(request):
    currencies = Currency.objects.all()
    price_list = []
    for currency in currencies:
        price = Price.objects.filter(currency_id=currency.pk).order_by('-created_at')[0]
        price_list.append(price)
        
    return render(request, 'main/home.html',{"price_list":price_list})

def detail(request, id):
    currency = Currency.objects.get(id=id)
    content = request.GET
    start_date = None
    end_date = None
    if 'endDate' in content:
        try:
            end_date = datetime.strptime(content['endDate'], '%Y-%m-%d')
        except Exception:
            pass
    if 'startDate' in content:
        try:
            start_date = datetime.strptime(content['startDate'], '%Y-%m-%d')
        except Exception:
            pass
    if start_date and end_date:
        data = Price.objects.filter(currency_id=currency.pk, created_at__lte = end_date, created_at__gte = start_date)
        if len(data) > 0:
            serialized_queryset = serializers.serialize('json', data)
            return render(request, 'main/detail.html',{'currency':currency, 'content':content, 'data': serialized_queryset})
    if start_date:
        data = Price.objects.filter(currency_id=currency.pk, created_at__gte = start_date)
        if len(data) > 0:
            serialized_queryset = serializers.serialize('json', data)
            return render(request, 'main/detail.html',{'currency':currency, 'content':content, 'data': serialized_queryset})
    today = datetime.now()
    limit_date = today + relativedelta(months=-1)
    data = Price.objects.filter(currency_id=currency.pk, created_at__gte = limit_date)
    if len(data) > 0:
        serialized_queryset = serializers.serialize('json', data)
        return render(request, 'main/detail.html',{'currency':currency, 'content':content, 'data': serialized_queryset})
    else:
        return render(request, 'main/detail.html',{'currency':currency, 'content':content, 'data': []})
            
    

def scrape_data(symbol, interval, ra):
    cur_url = api_url.format(symbol, interval, ra)
    print(cur_url)
    source = requests.get(cur_url).text
    res_json = json.loads(source)
    meta = res_json['chart']['result'][0]['meta']
    price = meta['regularMarketPrice']
    previous_price = meta['chartPreviousClose']
    change = round(float(price) - float(previous_price),4)
    changePer = round(change*100/float(price), 4);
    print([price,previous_price,change,changePer])
    
    return [price,previous_price,change,changePer]

def update_db(request):
    currencies = Currency.objects.all()
    for currency in currencies:
        res_15m = scrape_data(currency.symbol, "15m","15m")
        res_30m = scrape_data(currency.symbol, "30m","30m")
        res_60m = scrape_data(currency.symbol, "60m","60m")
        res_90m = scrape_data(currency.symbol, "90m","90m")
        res_1h = scrape_data(currency.symbol, "1h","1h")
        res_1d = scrape_data(currency.symbol, "1d","1d")
        res_5d = scrape_data(currency.symbol, "5d","5d")
        res_1w = scrape_data(currency.symbol, "1wk","1wk")
        res_1mo = scrape_data(currency.symbol, "1mo","1mo")
        res_3mo = scrape_data(currency.symbol, "3mo","3mo")
        res_6mo = scrape_data(currency.symbol, "3mo","6mo")
        res_1y = scrape_data(currency.symbol, "3mo","1y")
        res_2y = scrape_data(currency.symbol, "3mo","2y")
        price = Price(
            currency = currency, 
            l_15m_price = res_15m[0], 
            l_15m_prev = res_15m[1], 
            l_15m_change = res_15m[2], 
            l_15m_per = res_15m[3], 
            
            l_30m_price = res_30m[0], 
            l_30m_prev = res_30m[1], 
            l_30m_change = res_30m[2], 
            l_30m_per = res_30m[3], 

            l_60m_price = res_60m[0], 
            l_60m_prev = res_60m[1], 
            l_60m_change = res_60m[2], 
            l_60m_per = res_60m[3], 

            l_90m_price = res_90m[0], 
            l_90m_prev = res_90m[1], 
            l_90m_change = res_90m[2], 
            l_90m_per = res_90m[3], 

            l_1h_price = res_1h[0], 
            l_1h_prev = res_1h[1], 
            l_1h_change = res_1h[2],
            l_1h_per = res_1h[3], 

            l_1d_price = res_1d[0], 
            l_1d_prev = res_1d[1], 
            l_1d_change = res_1d[2], 
            l_1d_per = res_1d[3], 

            l_5d_price = res_5d[0], 
            l_5d_prev = res_5d[1], 
            l_5d_change = res_5d[2], 
            l_5d_per = res_5d[3], 

            l_1w_price = res_1w[0], 
            l_1w_prev = res_1w[1], 
            l_1w_change = res_1w[2], 
            l_1w_per = res_1w[3], 

            l_1mo_price = res_1mo[0], 
            l_1mo_prev = res_1mo[1], 
            l_1mo_change = res_1mo[2], 
            l_1mo_per = res_1mo[3], 

            l_3mo_price = res_3mo[0], 
            l_3mo_prev = res_3mo[1], 
            l_3mo_change = res_3mo[2], 
            l_3mo_per = res_3mo[3], 

            l_6mo_price = res_6mo[0], 
            l_6mo_prev = res_6mo[1], 
            l_6mo_change = res_6mo[2], 
            l_6mo_per = res_6mo[3], 

            l_1y_price = res_1y[0], 
            l_1y_prev = res_1y[1], 
            l_1y_change = res_1y[2], 
            l_1y_per = res_1y[3], 
            
            l_2y_price = res_2y[0], 
            l_2y_prev = res_2y[1], 
            l_2y_change = res_2y[2], 
            l_2y_per = res_2y[3]
            )
        price.save()
    response = {}
    response['status'] = 'success'
    return HttpResponse(json.dumps(response),content_type="application/json")
        
    
def get_prices(request):
    interval = request.GET['interval']
    price_json = []
    symbols = []
    currencies = Currency.objects.all()
    for currency in currencies:
        symbols.append(currency.symbol)
    p = Pool(10)
    price_json = p.map(scrape_data, symbols)
    return JsonResponse(price_json, safe=False)
    
