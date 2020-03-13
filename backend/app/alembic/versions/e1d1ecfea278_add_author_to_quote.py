"""add author to quote

Revision ID: e1d1ecfea278
Revises: 1080292cf115
Create Date: 2020-03-13 13:48:32.439924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1d1ecfea278'
down_revision = '1080292cf115'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quote', sa.Column('author', sa.String(), nullable=True))
    op.create_index(op.f('ix_quote_author'), 'quote', ['author'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quote_author'), table_name='quote')
    op.drop_column('quote', 'author')
    # ### end Alembic commands ###
