from flask import Flask, jsonify, redirect
from flask_restful import Api, MethodNotAllowed, NotFound
from flask_cors import CORS
from util.common import domain, port, prefix, build_swagger_config_json
from resource.swaggerConfig import SwaggerConfig
from resource.bookResource import BooksGETResource, BookGETResource, BookPOSTResource, BookPUTResource, BookDELETEResource
from flask_swagger_ui import get_swaggerui_blueprint
from models.bookModels import db
from util.common import db_uri



application = Flask(__name__)
app = application
app.config['PROPAGATE_EXCEPTIONS'] = True
CORS(app)
api = Api(app, prefix=prefix, catch_all_404s=True)

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()



build_swagger_config_json()
swaggerui_blueprint = get_swaggerui_blueprint(
    prefix,
    f'http://{domain}:{port}{prefix}/swagger-config',
    config={
        'app_name': "Flask API",
        "layout": "BaseLayout",
        "docExpansion": "none"
    },
)
app.register_blueprint(swaggerui_blueprint)




@app.errorhandler(NotFound)
def handle_method_not_found(e):
    response = jsonify({"message": str(e)})
    response.status_code = 404
    return response


@app.errorhandler(MethodNotAllowed)
def handle_method_not_allowed_error(e):
    response = jsonify({"message": str(e)})
    response.status_code = 405
    return response


@app.route('/')
def redirect_to_prefix():
    if prefix != '':
        return redirect(prefix)



api.add_resource(SwaggerConfig, '/swagger-config')

api.add_resource(BooksGETResource, '/books')
api.add_resource(BookGETResource, '/books/<int:id>')

api.add_resource(BookPOSTResource, '/books')

api.add_resource(BookPUTResource, '/books/<int:id>')

api.add_resource(BookDELETEResource, '/books/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)