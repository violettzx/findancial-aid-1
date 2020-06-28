"""empty message

Revision ID: e7372cbcf2bb
Revises: 
Create Date: 2020-06-27 21:41:01.748825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7372cbcf2bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user') as batch_op:
        batch_op.add_column(sa.Column('favourites', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'favourites')
    # ### end Alembic commands ###
