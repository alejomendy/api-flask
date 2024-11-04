from . import db

# Modelo Marca
class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)

    # Relación con Modelo (uno a muchos)
    modelos = db.relationship('Modelo', backref='marca', lazy=True)

# Modelo Fabricante
class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    pais_origen = db.Column(db.String(80))

    # Relación con Modelo (uno a muchos)
    modelos = db.relationship('Modelo', backref='fabricante', lazy=True)

# Modelo Modelo
class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)

    # Relaciones con Marca y Fabricante
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)

    # Relación con Equipo (uno a muchos)
    equipos = db.relationship('Equipo', backref='modelo', lazy=True)

# Modelo Característica
class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(200))

    # Relación con Equipo (uno a muchos)
    equipos = db.relationship('Equipo', backref='caracteristica', lazy=True)

# Modelo Equipo
class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    costo = db.Column(db.Float, nullable=False)

    # Relaciones con Modelo y Característica
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'))

    # Relación con Stock (uno a uno)
    stock = db.relationship('Stock', backref='equipo', uselist=False)

# Modelo Stock
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(80))

    # Relación con Equipo
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)

# Modelo Proveedor
class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    contacto = db.Column(db.String(120))

    # Relación con Accesorio (uno a muchos)
    accesorios = db.relationship('Accesorio', backref='proveedor', lazy=True)

# Modelo Accesorio
class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(80), nullable=False)
    compatible_con_modelos = db.Column(db.String(200))

    # Relación con Proveedor
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
