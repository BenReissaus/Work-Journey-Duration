"""Create Location and Journey Tables

Revision ID: eff8e241ff35
Revises: 
Create Date: 2018-01-31 15:26:23.330102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eff8e241ff35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alias', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('alias')
    )
    op.create_table('journey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('origin_id', sa.Integer(), nullable=False),
    sa.Column('destination_id', sa.Integer(), nullable=False),
    sa.Column('departure_time', sa.DateTime(), nullable=False),
    sa.Column('departure_quarter', sa.Integer(), nullable=False),
    sa.Column('departure_hour', sa.Integer(), nullable=False),
    sa.Column('travel_duration', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['destination_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['origin_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journey')
    op.drop_table('location')
    # ### end Alembic commands ###
