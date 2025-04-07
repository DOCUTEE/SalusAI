from app import create_app
from flask_cors import CORS
import socket


app = create_app()

CORS(app, origins=["http://localhost:5173"], supports_credentials=True)

if __name__ == '__main__':
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    app.run(debug=True, host=local_ip, port=8080)
