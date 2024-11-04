from flask import  render_template, Blueprint,request, redirect, url_for, flash,jsonify
from app import app, db
from app.models import Equipo, Modelo, Marca, Fabricante, Caracteristica, Stock, Proveedor, Accesorio
from .schemas import EquipoSchema
app = Blueprint('app', __name__)

equipo_schema = EquipoSchema()
equipos_schema = EquipoSchema(many=True)

# @app.route('/test', methods=['GET'])
# def test():
#     data = {
#         "message": "Bienvenido a la API",
#         "status": "success"
#     }
#     return jsonify(data)

@app.route('/api/test', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenido a la API", "status": "success"})


@app.route('/api/equipos', methods=['GET'])
def list_equipos():
    equipos = Equipo.query.all()
    return equipos_schema.jsonify(equipos)

@app.route('/api/modelos', methods=['GET'])
def list_modelos():
    modelos = Modelo.query.all()
    return jsonify([modelo.to_dict() for modelo in modelos])

@app.route('/api/marcas', methods=['GET'])
def list_marcas():
    marcas = Marca.query.all()
    return jsonify([marca.to_dict() for marca in marcas])

@app.route('/api/fabricantes', methods=['GET'])
def list_fabricantes():
    fabricantes = Fabricante.query.all()
    return jsonify([fabricante.to_dict() for fabricante in fabricantes])

@app.route('/api/caracteristicas', methods=['GET'])
def list_caracteristicas():
    caracteristicas = Caracteristica.query.all()
    return jsonify([caracteristica.to_dict() for caracteristica in caracteristicas])

@app.route('/api/stock', methods=['GET'])
def list_stock():
    stock_items = Stock.query.all()
    return jsonify([stock.to_dict() for stock in stock_items])

@app.route('/api/proveedores', methods=['GET'])
def list_proveedores():
    proveedores = Proveedor.query.all()
    return jsonify([proveedor.to_dict() for proveedor in proveedores])

@app.route('/api/accesorios', methods=['GET'])
def list_accesorios():
    accesorios = Accesorio.query.all()
    return jsonify([accesorio.to_dict() for accesorio in accesorios])



#RUTAS PARA LA CREACION

@app.route('/api/equipos', methods=['POST'])
def create_equipo():
    data = request.get_json()
    nuevo_equipo = Equipo(**data)
    db.session.add(nuevo_equipo)
    db.session.commit()
    return jsonify(nuevo_equipo.to_dict()), 201

@app.route('/api/modelos', methods=['POST'])
def create_modelo():
    data = request.get_json()
    nuevo_modelo = Modelo(**data)
    db.session.add(nuevo_modelo)
    db.session.commit()
    return jsonify(nuevo_modelo.to_dict()), 201

@app.route('/api/marcas', methods=['POST'])
def create_marca():
    data = request.get_json()
    nueva_marca = Marca(**data)
    db.session.add(nueva_marca)
    db.session.commit()
    return jsonify(nueva_marca.to_dict()), 201

@app.route('/api/fabricantes', methods=['POST'])
def create_fabricante():
    data = request.get_json()
    nuevo_fabricante = Fabricante(**data)
    db.session.add(nuevo_fabricante)
    db.session.commit()
    return jsonify(nuevo_fabricante.to_dict()), 201

@app.route('/api/caracteristicas', methods=['POST'])
def create_caracteristica():
    data = request.get_json()
    nueva_caracteristica = Caracteristica(**data)
    db.session.add(nueva_caracteristica)
    db.session.commit()
    return jsonify(nueva_caracteristica.to_dict()), 201

@app.route('/api/stock', methods=['POST'])
def create_stock():
    data = request.get_json()
    nuevo_stock = Stock(**data)
    db.session.add(nuevo_stock)
    db.session.commit()
    return jsonify(nuevo_stock.to_dict()), 201

@app.route('/api/proveedores', methods=['POST'])
def create_proveedor():
    data = request.get_json()
    nuevo_proveedor = Proveedor(**data)
    db.session.add(nuevo_proveedor)
    db.session.commit()
    return jsonify(nuevo_proveedor.to_dict()), 201

@app.route('/api/accesorios', methods=['POST'])
def create_accesorio():
    data = request.get_json()
    nuevo_accesorio = Accesorio(**data)
    db.session.add(nuevo_accesorio)
    db.session.commit()
    return jsonify(nuevo_accesorio.to_dict()), 201


#RUTAS PARA ELIMINAR

@app.route('/api/equipos/<int:id>', methods=['DELETE'])
def delete_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return jsonify({"message": "Equipo eliminado con éxito"}), 204

@app.route('/api/modelos/<int:id>', methods=['DELETE'])
def delete_modelo(id):
    modelo = Modelo.query.get_or_404(id)
    db.session.delete(modelo)
    db.session.commit()
    return jsonify({"message": "Modelo eliminado con éxito"}), 204

@app.route('/api/marcas/<int:id>', methods=['DELETE'])
def delete_marca(id):
    marca = Marca.query.get_or_404(id)
    db.session.delete(marca)
    db.session.commit()
    return jsonify({"message": "Marca eliminada con éxito"}), 204

@app.route('/api/fabricantes/<int:id>', methods=['DELETE'])
def delete_fabricante(id):
    fabricante = Fabricante.query.get_or_404(id)
    db.session.delete(fabricante)
    db.session.commit()
    return jsonify({"message": "Fabricante eliminado con éxito"}), 204

@app.route('/api/caracteristicas/<int:id>', methods=['DELETE'])
def delete_caracteristica(id):
    caracteristica = Caracteristica.query.get_or_404(id)
    db.session.delete(caracteristica)
    db.session.commit()
    return jsonify({"message": "Característica eliminada con éxito"}), 204

@app.route('/api/stock/<int:id>', methods=['DELETE'])
def delete_stock(id):
    stock = Stock.query.get_or_404(id)
    db.session.delete(stock)
    db.session.commit()
    return jsonify({"message": "Stock eliminado con éxito"}), 204

@app.route('/api/proveedores/<int:id>', methods=['DELETE'])
def delete_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return jsonify({"message": "Proveedor eliminado con éxito"}), 204

@app.route('/api/accesorios/<int:id>', methods=['DELETE'])
def delete_accesorio(id):
    accesorio = Accesorio.query.get_or_404(id)
    db.session.delete(accesorio)
    db.session.commit()
    return jsonify({"message": "Accesorio eliminado con éxito"}), 204

#RUTAS PARA LA EDICION

@app.route('/api/equipos/<int:id>', methods=['PUT'])
def edit_equipo_view(id):
    equipo = Equipo.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(equipo, key, value)
    db.session.commit()
    return jsonify(equipo.to_dict()), 200

@app.route('/api/modelos/<int:id>', methods=['PUT'])
def edit_modelo_view(id):
    modelo = Modelo.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(modelo, key, value)
    db.session.commit()
    return jsonify(modelo.to_dict()), 200

@app.route('/api/marcas/<int:id>', methods=['PUT'])
def edit_marca_view(id):
    marca = Marca.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(marca, key, value)
    db.session.commit()
    return jsonify(marca.to_dict()), 200

@app.route('/api/fabricantes/<int:id>', methods=['PUT'])
def edit_fabricante_view(id):
    fabricante = Fabricante.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(fabricante, key, value)
    db.session.commit()
    return jsonify(fabricante.to_dict()), 200

@app.route('/api/caracteristicas/<int:id>', methods=['PUT'])
def edit_caracteristica_view(id):
    caracteristica = Caracteristica.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(caracteristica, key, value)
    db.session.commit()
    return jsonify(caracteristica.to_dict()), 200

@app.route('/api/stock/<int:id>', methods=['PUT'])
def edit_stock_view(id):
    stock = Stock.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(stock, key, value)
    db.session.commit()
    return jsonify(stock.to_dict()), 200

@app.route('/api/proveedores/<int:id>', methods=['PUT'])
def edit_proveedor_view(id):
    proveedor = Proveedor.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(proveedor, key, value)
    db.session.commit()
    return jsonify(proveedor.to_dict()), 200

@app.route('/api/accesorios/<int:id>', methods=['PUT'])
def edit_accesorio_view(id):
    accesorio = Accesorio.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(accesorio, key, value)
    db.session.commit()
    return jsonify(accesorio.to_dict()), 200
