from flask import Flask

# Bibliotecas publicamente acessíveis
#db = SQLAlchemy()

def init_app():
    # Inicializa a aplicação
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Inicializa Plugins
    #db.init_app(app)

    with app.app_context():
        # Inclui as routes
        from . import routes

        # Registra blueprints
        #app.register_blueprint(auth.auth_bp)

        return app