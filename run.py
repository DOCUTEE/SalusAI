from app import create_app
from flask_cors import CORS


app = create_app()

CORS(app, origins=["http://localhost:5173"], supports_credentials=True)

if __name__ == '__main__':
    app.run(debug=True,host ="192.168.124.254",port=8080)
