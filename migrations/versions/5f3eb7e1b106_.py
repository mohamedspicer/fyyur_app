"""empty message

Revision ID: 5f3eb7e1b106
Revises: c7405f32988e
Create Date: 2021-07-04 17:02:39.887305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f3eb7e1b106'
down_revision = 'c7405f32988e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'cities', ['state'])
    op.create_unique_constraint(None, 'cities', ['city'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cities', type_='unique')
    op.drop_constraint(None, 'cities', type_='unique')
    # ### end Alembic commands ###
