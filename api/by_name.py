from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        s = self.path
        print("s:", s)
        url_components = parse.urlsplit(s)
        print("url_components:", url_components)
        query_string_list = parse.parse_qsl(url_components.query)
        print("url_components.query:", url_components.query)
        print("query_string_list:", query_string_list)
        query_dict = dict(query_string_list)
        print("query_dict:", query_dict)
        url = "https://restcountries.com/v3.1/"
        country = query_dict["name"]
        
        if country:
            r = requests.get(url + "name/" + country)
            print("response:", r)
            if r.status_code == 404:
                message = "Please enter a valid country."
                print("invalid country message:", message)
                self.send_response(404)
                self.send_header('Content-type','text/plain')
                self.end_headers()
                self.wfile.write(message.encode('utf-8'))
                return
            
            data = r.json()
            print("data:", data)
            capital = data[0]["capital"][0]
            print("capital:", capital)
            message = f"The capital of {country} is {capital}."
            print("message:", message)
        
        else:
            message = "Please enter a country."
            print("missing country message:", message)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return
