import urllib.request
import json

URL_API = 'http://api.minfin.com.ua/mb/60524bef48e4525b3fb1622f5ad24ce55dde7020/'

def request_rate():
    request = urllib.request.Request(URL_API)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode('utf-8'))
    return round(float(data[2]['ask']), 1)
