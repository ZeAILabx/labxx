from flask import Flask, request, jsonify
from flask_cors import CORS
from src.config import Config
from src.routes.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/api/*": {"origins": Config.CORS_ORIGINS}}, supports_credentials=True)

    @app.before_request
    def handle_options_preflight():
        if request.method == 'OPTIONS':
            response = app.make_default_options_response()
            response.status_code = 200
            return response

    register_routes(app)

    @app.route('/api/health')
    def health():
        return {'success': True, 'data': {'status': 'healthy'}}

    # Ensure all rules accept OPTIONS method for CORS preflights
    for rule in app.url_map.iter_rules():
        if rule.methods:
            rule.methods.add('OPTIONS')

    return app
