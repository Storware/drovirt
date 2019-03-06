"""server default create

Revision ID: 9fff690a1c24
Revises: 440caa4f4e01
Create Date: 2019-01-22 04:48:28.378173

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9fff690a1c24'
down_revision = '440caa4f4e01'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('cluster', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text('now()'),
               existing_nullable=False)
    op.alter_column('datacenter', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text('now()'),
               existing_nullable=False)
    op.alter_column('hypervisor', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text('now()'),
               existing_nullable=False)
    op.alter_column('hypervisor_manager', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text('now()'),
               existing_nullable=False)
    op.alter_column('node', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text('now()'),
               existing_nullable=False)
    op.add_column('task', sa.Column('updated', sa.DateTime(), nullable=True))
    op.alter_column('task', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text('now()'),
               nullable=True)
    op.alter_column('task_group', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text('now()'),
               existing_nullable=False)
    op.alter_column('vm', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text('now()'),
               existing_nullable=False)


def downgrade():
    op.alter_column('vm', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('task_group', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('task', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               nullable=False)
    op.drop_column('task', 'updated')
    op.alter_column('node', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('hypervisor_manager', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('hypervisor', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('datacenter', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('cluster', 'created',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               existing_nullable=False)
