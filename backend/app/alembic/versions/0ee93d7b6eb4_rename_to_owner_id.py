"""rename to owner_id

Revision ID: 0ee93d7b6eb4
Revises: 2ef950e658f9
Create Date: 2020-03-07 20:58:36.358018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ee93d7b6eb4'
down_revision = '2ef950e658f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.drop_constraint('tag_parent_id_fkey', 'tag', type_='foreignkey')
    op.create_foreign_key(None, 'tag', 'tag', ['owner_id'], ['id'])
    op.drop_column('tag', 'parent_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'tag', type_='foreignkey')
    op.create_foreign_key('tag_parent_id_fkey', 'tag', 'tag', ['parent_id'], ['id'])
    op.drop_column('tag', 'owner_id')
    # ### end Alembic commands ###
