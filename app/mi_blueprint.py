from flask import Blueprint

#crear y configurar el blueprint
mi_blueprint= Blueprint("mi_blueprint", __name__, url_prefix = '/ejemplo')

#crear ruta de ejemplo para el blueprint
@mi_blueprint.route('/hola')
def saludo():
    return 'hola mundo'