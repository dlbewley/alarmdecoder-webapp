"""Camera support

Revision ID: 4a5a64ce67ac
Revises: 2d5cbdadf755
Create Date: 2015-01-15 11:15:53.410793

"""

# revision identifiers, used by Alembic.
revision = '4a5a64ce67ac'
down_revision = '2d5cbdadf755'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cameras',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=32), nullable=False),
    sa.Column('username', sa.VARCHAR(length=32)),
    sa.Column('password', sa.VARCHAR(length=255)),
    sa.Column('get_jpg_url', sa.VARCHAR(length=255), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cameras')
    ### end Alembic commands ###
