from http.server import BaseHTTPRequestHandler, HTTPServer

# Definimos una clase que maneja las solicitudes HTTP
class MiServidor(BaseHTTPRequestHandler):
    def do_GET(self):
        # Indicamos que la respuesta fue exitosa (código 200)
        self.send_response(200)
        # Indicamos el tipo de contenido que se enviará (HTML)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # Escribimos el contenido de la página
        self.wfile.write(b"<html><body><h1>Hola Mundo</h1></body></html>")

# Configuramos el servidor
if __name__ == "__main__":
    host = "localhost"
    port = 8080
    servidor = HTTPServer((host, port), MiServidor)
    print(f"Servidor iniciado en http://{host}:{port}")
    print("Presiona Ctrl+C para detenerlo.")
    servidor.serve_forever()
