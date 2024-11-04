from app.app import create_app, db
from app.models import Equipo

app = create_app()

with app.app_context():
    db.create_all()
    if Equipo.query.count() == 0:
        equipos = [
            Equipo(nombre='Samsung Galaxy S21', modelo='S21', categoria='Smartphone', costo=799.99),
            Equipo(nombre='iPhone 13', modelo='13', categoria='Smartphone', costo=999.99)
        ]
        db.session.bulk_save_objects(equipos)
        db.session.commit()
        print("Data seeded.")
    else:
        print("Database already contains data.")
