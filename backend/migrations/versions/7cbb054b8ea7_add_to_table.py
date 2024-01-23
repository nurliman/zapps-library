"""add  to  table

Revision ID: 7cbb054b8ea7
Revises: 42b7603cc6f6
Create Date: 2024-01-23 15:08:25.164939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cbb054b8ea7'
down_revision = '42b7603cc6f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.Enum('SUPERUSER', 'ADMIN', 'MEMBER', name='userrole'), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###
