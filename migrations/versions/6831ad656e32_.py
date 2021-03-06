"""empty message

Revision ID: 6831ad656e32
Revises: 59eea83e34d1
Create Date: 2021-07-04 01:43:22.028513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6831ad656e32'
down_revision = '59eea83e34d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.String(length=120), nullable=False))
    op.drop_column('venues', 'geners')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('geners', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###
