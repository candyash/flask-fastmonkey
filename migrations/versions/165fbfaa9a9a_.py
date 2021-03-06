"""empty message

Revision ID: 165fbfaa9a9a
Revises: 4f796700409b
Create Date: 2014-10-12 13:44:41.588587

"""

# revision identifiers, used by Alembic.
revision = '165fbfaa9a9a'
down_revision = '4f796700409b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    op.add_column(u'friends', sa.Column('bestfriend', sa.Boolean(), nullable=True))
    op.add_column(u'friends', sa.Column('friend_account', sa.Integer(), nullable=True))
    op.drop_column(u'friends', 'status')
    op.drop_column(u'friends', 'friend_accunt')
    op.add_column(u'users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'users', 'last_seen')
    op.add_column(u'friends', sa.Column('friend_accunt', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column(u'friends', sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column(u'friends', 'friend_account')
    op.drop_column(u'friends', 'bestfriend')
    op.drop_table('followers')
    ### end Alembic commands ###
