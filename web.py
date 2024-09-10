from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

routes = {
    '/proyecto/web-uno': lambda params: f'<h1>Proyecto: web-uno Autor: {params.get("Abraham")}</h1>'
}

class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        if self.path == '/':
            try:
                with open('home.html', 'r') as f:
                    content = f.read()
            except FileNotFoundError:
                content = "<h1>Archivo home.html no encontrado</h1>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))
          

    def get_response(self):
        return f"""
        <h1> Hola Web </h1>  
        <p> From Request: </p>
        <ul>
            <li> Host: {self.headers.get('Host')} </li>
            <li> User-Agent: {self.headers.get('User-Agent')} </li>
            <li> Requested Path: {self.path} </li>
        </ul>
            <p> From Response: </p>
        <ul>
            <li> Content-Type: {self.headers.get('Content-Type')} </li>
            <li> Server: {self.headers.get('Server')} </li>
            <li> Date: {self.headers.get('Date')} </li>
        </ul>
    """
        
        def get_response(self):

            path = self.url().path
            params = self.query_data()
            response_function = routes.get(path)
        if response_function:
            return response_function(params)
        else:
            return "<h1>Ruta no encontrada</h1>"


if __name__ == "__main__":
 # Especificamos el puerto
    port = 8000
    server_address = ('localhost', port)

    # Creamos el servidor y lo iniciamos
    httpd = HTTPServer(server_address, WebRequestHandler)
    print(f"Servidor iniciado en http://localhost:{port}")
    httpd.serve_forever()
