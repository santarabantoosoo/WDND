import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify
import json

app = Flask(__name__)

spec = APISpec(
    title="Swagger Example",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

@app.route("/version")
def get_info():
    """
    Get info on our server
    ---
    get:
        description: Get the version information for our service
        responses:
            200:
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                version:
                                    type: string
                                    description: Version number of our service
    """
    return jsonify({
        "version": os.environ.get("VERSION"),
    })


# Need to register the path
with app.test_request_context():
    spec.path(view=get_info)

with open('swagger.json', 'w') as f:
    json.dump(spec.to_dict(), f)

# @app.route("/spec")
# def get_apispec():
#     return jsonify(spec.to_dict())

