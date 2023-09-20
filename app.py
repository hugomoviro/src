from flask import Flask
from views import blueprint
from flasgger import Swagger

# pip install flasgger
app = Flask(__name__)
swagger = Swagger(app)
app.register_blueprint(blueprint=blueprint)



if __name__ == '__main__':
    app.run(debug=True)