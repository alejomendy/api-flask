from flask_marshmallow import Marshmallow

from marshmallow import Schema, fields

ma = Marshmallow()

class EquipoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    costo = fields.Float(required=True)  
    modelo_id = fields.Int(required=True)
    marca_id = fields.Int(required=False)  
   

class ModeloSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    marca_id = fields.Int(required=True)
    fabricante_id = fields.Int(required=True)
    

class MarcaSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str(allow_none=True)  

class FabricanteSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    pais_origen = fields.Str(required=True)
    
class CaracteristicaSchema(Schema):
    id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True)
    descripcion = fields.Str(required=True)

class StockSchema(Schema):
    id = fields.Int(dump_only=True)
    cantidad_disponible = fields.Int(required=True)
    ubicacion = fields.Str(required=True)
    equipo_id = fields.Int(required=True)

class ProveedorSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    contacto = fields.Str(allow_none=True)  

class AccesorioSchema(Schema):
    id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True)
    compatible_con_modelos = fields.Str(allow_none=True)  
    proveedor_id = fields.Int(required=True)
