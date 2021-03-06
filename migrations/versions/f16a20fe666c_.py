"""empty message

Revision ID: f16a20fe666c
Revises: d4e6e6faacfb
Create Date: 2019-09-04 18:41:44.388024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f16a20fe666c'
down_revision = 'd4e6e6faacfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('leagues', sa.Column('season', sa.Integer(), server_default='2019', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('leagues', 'season')
    # ### end Alembic commands ###
