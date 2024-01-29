from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
 
    def do_GET_capital(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        query_dict = dict(query_string_list)
        url = "https://restcountries.com/v3.1/"

        if "capital" in query_dict:
            capital = query_dict["capital"]
            r = requests.get(url + query_string_list + "capital/" + capital)
            data = r.json()
            country = data.data.name.common
            message = "", capital, "is the capital of", country,"."
            print(r)
        
        if "country" in query_dict:
            country = query_dict["country"]
            r = requests.get(url + query_string_list + "country/" + country)
            data = r.json()
            capital= data.data.capital
            message = "The capital of", country, "is",capital,"."
            print(r)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        
        self.wfile.write(message)