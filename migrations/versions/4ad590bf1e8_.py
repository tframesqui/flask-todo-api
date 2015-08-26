"""empty message

Revision ID: 4ad590bf1e8
Revises: de61712128
Create Date: 2015-08-26 08:38:09.399229

"""

# revision identifiers, used by Alembic.
revision = '4ad590bf1e8'
down_revision = 'de61712128'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('base')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('date_modified', sa.DATETIME(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('done', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Item')
    ### end Alembic commands ###
