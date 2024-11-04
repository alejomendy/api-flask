"""create tablas equipos

Revision ID: 44e6589bfa36
Revises: 
Create Date: 2024-11-04 16:35:43.836763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44e6589bfa36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caracteristica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=80), nullable=False),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fabricante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('pais_origen', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proveedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('contacto', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('accesorio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=80), nullable=False),
    sa.Column('compatible_con_modelos', sa.String(length=200), nullable=True),
    sa.Column('proveedor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['proveedor_id'], ['proveedor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modelo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('marca_id', sa.Integer(), nullable=False),
    sa.Column('fabricante_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fabricante_id'], ['fabricante.id'], ),
    sa.ForeignKeyConstraint(['marca_id'], ['marca.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('costo', sa.Float(), nullable=False),
    sa.Column('modelo_id', sa.Integer(), nullable=False),
    sa.Column('caracteristica_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['caracteristica_id'], ['caracteristica.id'], ),
    sa.ForeignKeyConstraint(['modelo_id'], ['modelo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cantidad_disponible', sa.Integer(), nullable=False),
    sa.Column('ubicacion', sa.String(length=80), nullable=True),
    sa.Column('equipo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['equipo_id'], ['equipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    op.drop_table('equipo')
    op.drop_table('modelo')
    op.drop_table('accesorio')
    op.drop_table('proveedor')
    op.drop_table('marca')
    op.drop_table('fabricante')
    op.drop_table('caracteristica')
    # ### end Alembic commands ###
