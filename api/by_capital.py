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
        capital = query_dict["capital"]
        
        if capital:
            r = requests.get(url + "capital/" + capital)
            print("response:", r)
            if r.status_code == 404:
                message = "Please enter a valid capital."
                print("invalid capital message:", message)
                self.send_response(404)
                self.send_header('Content-type','text/plain')
                self.end_headers()
                self.wfile.write(message.encode('utf-8'))
                return
            
            data = r.json()
            print("data:", data)
            country = data[0]["name"]["common"]
            print("country:", country)
            message = f"{capital} is the capital of {country}."
            print("message:", message)
        
        else:
            message = "Please enter a capital."
            print("missing capital message:", message)
            return print(message)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return
    