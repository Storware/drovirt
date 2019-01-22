"""empty message

Revision ID: 51c0570aa30e
Revises: 4c099ca726ca
Create Date: 2019-01-05 02:51:50.462690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51c0570aa30e'
down_revision = '4c099ca726ca'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('vm', sa.Column('cluster_id', sa.Integer(), nullable=False))
    op.add_column('vm', sa.Column('datacenter_id', sa.Integer(), nullable=False))
    op.add_column('vm', sa.Column('hypervisor_id', sa.Integer(), nullable=False))
    op.add_column('vm', sa.Column('hypervisor_manager_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'vm', 'hypervisor_manager', ['hypervisor_manager_id'], ['id'])
    op.create_foreign_key(None, 'vm', 'cluster', ['cluster_id'], ['id'])
    op.create_foreign_key(None, 'vm', 'datacenter', ['datacenter_id'], ['id'])
    op.create_foreign_key(None, 'vm', 'hypervisor', ['hypervisor_id'], ['id'])


def downgrade():
    op.drop_constraint(None, 'vm', type_='foreignkey')
    op.drop_constraint(None, 'vm', type_='foreignkey')
    op.drop_constraint(None, 'vm', type_='foreignkey')
    op.drop_constraint(None, 'vm', type_='foreignkey')
    op.drop_column('vm', 'hypervisor_manager_id')
    op.drop_column('vm', 'hypervisor_id')
    op.drop_column('vm', 'datacenter_id')
    op.drop_column('vm', 'cluster_id')
