"""Acquire VMs

Revision ID: 39fb3a858a98
Revises: 9fff690a1c24
Create Date: 2019-06-27 17:48:23.634424

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision = '39fb3a858a98'
down_revision = '9fff690a1c24'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('hypervisor_manager', sa.Column('allow_insecure', sa.Boolean(), nullable=False))
    op.add_column('hypervisor_manager', sa.Column('password', sa.String(length=256), nullable=False))
    op.add_column('hypervisor_manager', sa.Column('username', sa.String(length=256), nullable=False))
    op.add_column('vm', sa.Column('cpus', sa.Integer(), nullable=True))
    op.add_column('vm', sa.Column('memory', sa.Integer(), nullable=True))
    op.add_column('vm', sa.Column('status', sa.String(length=64), nullable=True))
    op.add_column('vm', sa.Column('vm_type', sa.String(length=64), nullable=True))

    taskstatus = postgresql.ENUM('QUEUED', 'ACTIVE', 'COMPLETED', 'FAILED', name='taskstatus')
    taskstatus.create(op.get_bind())

    op.alter_column('task', 'status',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.Enum('QUEUED', 'ACTIVE', 'COMPLETED', 'FAILED', name='taskstatus'),
               existing_nullable=False, postgresql_using='status::taskstatus')
    op.alter_column('vm', 'cluster_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('vm', 'datacenter_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('vm', 'hypervisor_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('vm', 'memory',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)


def downgrade():
    op.drop_column('vm', 'vm_type')
    op.drop_column('vm', 'status')
    op.drop_column('vm', 'memory')
    op.drop_column('vm', 'cpus')
    op.drop_column('hypervisor_manager', 'username')
    op.drop_column('hypervisor_manager', 'password')
    op.drop_column('hypervisor_manager', 'allow_insecure')

    op.alter_column('vm', 'memory',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    op.alter_column('vm', 'hypervisor_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('vm', 'datacenter_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('vm', 'cluster_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('task', 'status',
                    existing_type=sa.Enum('QUEUED', 'ACTIVE', 'COMPLETED', 'FAILED', name='taskstatus'),
                    #postgresql_using='status::taskstatus'
                    type_=sa.VARCHAR(length=16),
                    existing_nullable=False)

    taskstatus = postgresql.ENUM('QUEUED', 'ACTIVE', 'COMPLETED', 'FAILED', name='taskstatus')
    taskstatus.drop(op.get_bind())