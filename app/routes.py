from flask import Blueprint, request, jsonify
from app import db
from app.models import Equipo, Modelo, Marca, Fabricante, Caracteristica, Stock, Proveedor, Accesorio, Usuario
from .schemas import EquipoSchema, ModeloSchema, MarcaSchema, FabricanteSchema, CaracteristicaSchema, StockSchema, ProveedorSchema, AccesorioSchema, UsuarioSchema
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
api_bp = Blueprint('api', __name__)

# Configuración JWT
# app.config['JWT_SECRET_KEY'] = 'super-secret'  # clave
# jwt = JWTManager(app)

# Schemas
equipo_schema = EquipoSchema()
equipos_schema = EquipoSchema(many=True)
modelo_schema = ModeloSchema()
modelos_schema = ModeloSchema(many=True)
marca_schema = MarcaSchema()
marcas_schema = MarcaSchema(many=True)
fabricante_schema = FabricanteSchema()
fabricantes_schema = FabricanteSchema(many=True)
caracteristica_schema = CaracteristicaSchema()
caracteristicas_schema = CaracteristicaSchema(many=True)
stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)
proveedor_schema = ProveedorSchema()
proveedores_schema = ProveedorSchema(many=True)
accesorio_schema = AccesorioSchema()
accesorios_schema = AccesorioSchema(many=True)
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)



def create_object(model, schema):
    data = request.get_json()
    new_object = model(**data)
    db.session.add(new_object)
    db.session.commit()
    return jsonify(schema.dump(new_object)), 201

def delete_object(model, id):
    obj = model.query.get_or_404(id)
    db.session.delete(obj)
    db.session.commit()
    return jsonify({"message": f"{model.__name__} eliminado con éxito"}), 204

def update_object(model, schema, id):
    obj = model.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(obj, key, value)
    db.session.commit()
    return jsonify(schema.dump(obj)), 200


@api_bp.route('/test', methods=['GET'])
def test():
    data = {
        "message": "Bienvenido a la API",
        "status": "success"
    }
    return jsonify(data)


@api_bp.route('/api/test', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenido a la API", "status": "success"})


@api_bp.route('/equipos', methods=['GET'])
def list_equipos():
    equipos = Equipo.query.all()
    return jsonify(equipos_schema.dump(equipos))


@api_bp.route('/modelos', methods=['GET'])
def list_modelos():
    modelos = Modelo.query.all()
    return jsonify(modelos_schema.dump(modelos))


@api_bp.route('/marcas', methods=['GET'])
def list_marcas():
    marcas = Marca.query.all()
    return jsonify(marcas_schema.dump(marcas))


@api_bp.route('/fabricantes', methods=['GET'])
def list_fabricantes():
    fabricantes = Fabricante.query.all()
    return jsonify(fabricantes_schema.dump(fabricantes))


@api_bp.route('/caracteristicas', methods=['GET'])
def list_caracteristicas():
    caracteristicas = Caracteristica.query.all()
    return jsonify(caracteristicas_schema.dump(caracteristicas))


@api_bp.route('/stock', methods=['GET'])
def list_stock():
    stock = Stock.query.all()
    return jsonify(stocks_schema.dump(stock))


@api_bp.route('/proveedores', methods=['GET'])
def list_proveedores():
    proveedores = Proveedor.query.all()
    return jsonify(proveedores_schema.dump(proveedores))


@api_bp.route('/accesorios', methods=['GET'])
def list_accesorios():
    accesorios = Accesorio.query.all()
    return jsonify(accesorios_schema.dump(accesorios))

@api_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()  
    usuarios_schema = UsuarioSchema(many=True)  
    return jsonify(usuarios_schema.dump(usuarios)), 200



# Rutas para creación
@api_bp.route('/equipos', methods=['POST'])
def create_equipo():
    return create_object(Equipo, equipo_schema)

@api_bp.route('/modelos', methods=['POST'])
def create_modelo():
    return create_object(Modelo, modelo_schema)

@api_bp.route('/marcas', methods=['POST'])
def create_marca():
    return create_object(Marca, marca_schema)

@api_bp.route('/fabricantes', methods=['POST'])
def create_fabricante():
    return create_object(Fabricante, fabricante_schema)

@api_bp.route('/caracteristicas', methods=['POST'])
def create_caracteristica():
    return create_object(Caracteristica, caracteristica_schema)

@api_bp.route('/stock', methods=['POST'])
def create_stock():
    return create_object(Stock, stock_schema)

@api_bp.route('/proveedores', methods=['POST'])
def create_proveedor():
    return create_object(Proveedor, proveedor_schema)

@api_bp.route('/accesorios', methods=['POST'])
def create_accesorio():
    return create_object(Accesorio, accesorio_schema)

# Rutas para eliminación
@api_bp.route('/equipos/<int:id>', methods=['DELETE'])
def delete_equipo(id):
    return delete_object(Equipo, id)

@api_bp.route('/modelos/<int:id>', methods=['DELETE'])
def delete_modelo(id):
    return delete_object(Modelo, id)

@api_bp.route('/marcas/<int:id>', methods=['DELETE'])
def delete_marca(id):
    return delete_object(Marca, id)

@api_bp.route('/fabricantes/<int:id>', methods=['DELETE'])
def delete_fabricante(id):
    return delete_object(Fabricante, id)

@api_bp.route('/caracteristicas/<int:id>', methods=['DELETE'])
def delete_caracteristica(id):
    return delete_object(Caracteristica, id)

@api_bp.route('/stock/<int:id>', methods=['DELETE'])
def delete_stock(id):
    return delete_object(Stock, id)

@api_bp.route('/proveedores/<int:id>', methods=['DELETE'])
def delete_proveedor(id):
    return delete_object(Proveedor, id)

@api_bp.route('/accesorios/<int:id>', methods=['DELETE'])
def delete_accesorio(id):
    return delete_object(Accesorio, id)

@api_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    return delete_usuario(Usuario, id)

# Rutas para edición
@api_bp.route('/equipos/<int:id>', methods=['PUT'])
def edit_equipo_view(id):
    return update_object(Equipo, equipo_schema, id)

@api_bp.route('/modelos/<int:id>', methods=['PUT'])
def edit_modelo_view(id):
    return update_object(Modelo, modelo_schema, id)

@api_bp.route('/marcas/<int:id>', methods=['PUT'])
def edit_marca_view(id):
    return update_object(Marca, marca_schema, id)

@api_bp.route('/fabricantes/<int:id>', methods=['PUT'])
def edit_fabricante_view(id):
    return update_object(Fabricante, fabricante_schema, id)

@api_bp.route('/caracteristicas/<int:id>', methods=['PUT'])
def edit_caracteristica_view(id):
    return update_object(Caracteristica, caracteristica_schema, id)

@api_bp.route('/stock/<int:id>', methods=['PUT'])
def edit_stock_view(id):
    return update_object(Stock, stock_schema, id)

@api_bp.route('/proveedores/<int:id>', methods=['PUT'])
def edit_proveedor_view(id):
    return update_object(Proveedor, proveedor_schema, id)

@api_bp.route('/accesorios/<int:id>', methods=['PUT'])
def edit_accesorio_view(id):
    return update_object(Accesorio, accesorio_schema, id)

# RUTAS PARA USUARIOS

@api_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    
    if Usuario.query.filter_by(username=username).first():
        return jsonify({"error": "Usuario ya registrado"}), 400

    nuevo_usuario = Usuario(username=username, rol='User')  
    nuevo_usuario.set_password(password)
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return jsonify({"message": "Usuario creado con éxito"}), 201


@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    usuario = Usuario.query.filter_by(username=username).first()  
    if not usuario or not usuario.check_password(password):
        return jsonify({"error": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity={"id": usuario.id, "rol": usuario.rol}) 
    return jsonify(access_token=access_token), 200

@app.route('/api/usuarios/<int:id>', methods=['GET', 'PUT'])
def handle_user(id):
    if request.method == 'GET':
        return jsonify({"id": id, "username": "usuario_example"})  
    elif request.method == 'PUT':
        data = request.get_json()
        return jsonify({"message": f"Usuario {id} actualizado exitosamente"}), 200