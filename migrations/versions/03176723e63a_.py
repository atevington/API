"""empty message

Revision ID: 03176723e63a
Revises: 2259890fb9a3
Create Date: 2018-08-26 23:40:30.727399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03176723e63a'
down_revision = '2259890fb9a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('receive_notifications', sa.Boolean(), server_default='True', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'receive_notifications')
    # ### end Alembic commands ###