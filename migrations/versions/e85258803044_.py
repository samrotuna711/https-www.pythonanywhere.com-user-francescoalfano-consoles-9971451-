"""empty message

Revision ID: e85258803044
Revises: 49d9db3d2c50
Create Date: 2018-08-26 23:51:31.799647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e85258803044'
down_revision = '49d9db3d2c50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('comments', sa.Column('commenter_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['commenter_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'posted')
    op.drop_column('comments', 'commenter_id')
    op.drop_table('users')
    # ### end Alembic commands ###
