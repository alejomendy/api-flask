from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Marca(db.Model):
    __tablename__ = 'marca'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    modelos = db.relationship('Modelo', backref='marca', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }

class Fabricante(db.Model):
    __tablename__ = 'fabricante'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    pais_origen = db.Column(db.String(80))
    modelos = db.relationship('Modelo', backref='fabricante', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'pais_origen': self.pais_origen
        }

class Modelo(db.Model):
    __tablename__ = 'modelo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    equipos = db.relationship('Equipo', backref='modelo', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'marca_id': self.marca_id,
            'fabricante_id': self.fabricante_id
        }

class Caracteristica(db.Model):
    __tablename__ = 'caracteristica'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(200))
    equipos = db.relationship('Equipo', backref='caracteristica', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'descripcion': self.descripcion
        }

class Equipo(db.Model):
    __tablename__ = 'equipo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    costo = db.Column(db.Float, nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'))
    stock = db.relationship('Stock', backref='equipo', uselist=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'costo': self.costo,
            'modelo_id': self.modelo_id,
            'caracteristica_id': self.caracteristica_id,
            'stock': self.stock.to_dict() if self.stock else None
        }

class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(80))
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cantidad_disponible': self.cantidad_disponible,
            'ubicacion': self.ubicacion,
            'equipo_id': self.equipo_id
        }

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    contacto = db.Column(db.String(120))
    accesorios = db.relationship('Accesorio', backref='proveedor', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'contacto': self.contacto
        }

class Accesorio(db.Model):
    __tablename__ = 'accesorio'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(80), nullable=False)
    compatible_con_modelos = db.Column(db.String(200))
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'compatible_con_modelos': self.compatible_con_modelos,
            'proveedor_id': self.proveedor_id
        }

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(50), nullable=True, default='User')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'rol': self.rol
        }
    
    
