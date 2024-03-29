"""Initial migration

Revision ID: 7959eeaf8400
Revises: 
Create Date: 2024-02-15 13:58:34.894389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7959eeaf8400'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###
