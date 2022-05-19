from flask import Flask
from routes.api_routes import apiroutes
app = Flask(__name__)
app.config["SECRET_KEY"] = "TEST"

app.register_blueprint(apiroutes)
