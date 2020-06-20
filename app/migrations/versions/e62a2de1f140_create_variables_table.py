"""
create_variables_table

Revision ID: e62a2de1f140
Revises: 1e41e995e7c4
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision = 'e62a2de1f140'
down_revision = '1e41e995e7c4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('variables',
        sa.Column('id', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('min_value', sa.Float(), nullable=False),
        sa.Column('max_value', sa.Float(), nullable=False),
        sa.Column('device_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['device_id'], ['devices.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
   op.drop_table('variables')
