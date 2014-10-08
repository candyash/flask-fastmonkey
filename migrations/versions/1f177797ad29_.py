"""empty message

Revision ID: 1f177797ad29
Revises: 48147c019f38
Create Date: 2014-10-08 21:47:14.810248

"""

# revision identifiers, used by Alembic.
revision = '1f177797ad29'
down_revision = '48147c019f38'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.drop_column('users', 'active')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('users', 'is_active')
    ### end Alembic commands ###
