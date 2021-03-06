"""actually_add_seperate_user_foreign_key_in_tags

Revision ID: 39ce44cc5447
Revises: a7f8ce4c9061
Create Date: 2020-03-07 22:07:22.046944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39ce44cc5447'
down_revision = 'a7f8ce4c9061'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'tag', 'user', ['owner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tag', type_='foreignkey')
    # ### end Alembic commands ###
